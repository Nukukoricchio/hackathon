import logging
import math
import multiprocessing
from tqdm import tqdm

import torch
from torch.nn import functional as F
from transformers import AutoModel, AutoTokenizer
from contextlib import contextmanager


logger = logging.getLogger("Ranker")

@contextmanager
def ignored(*exceptions):
  try:
    yield
  except exceptions:
    pass 

class BaseRanker:
    def __init__(self, filter_dict: dict, device: str):
        self.device = device
        self.filter_dict = filter_dict
        self.weights = {}
        for k, v in filter_dict.items():
            self.weights[k] = int(v["priority"]) / 5

        self.phobert = AutoModel.from_pretrained("vinai/phobert-base").to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
    
    def get_phobert_embedding(self, sentence):
        input_ids = self.tokenizer.encode(sentence, return_tensors="pt").to(self.device)
        with torch.no_grad():
            feature = self.phobert(input_ids)[1]
        return feature

    def scoring_func(x, slope, power, center=0):
        return 1 / (1 + ((slope-center)/(x-center)**power))

    def scoring_age(self, cv):
        try:
            age_score = 1
            if cv["info_age"] not in range(self.filter_dict["req_age"]["min"], self.filter_dict["req_age"]["max"]):
                pivot = self.filter_dict["req_age"]["max"] \
                                if cv["info_age"] > self.filter_dict["req_age"]["max"] \
                                else self.filter_dict["req_age"]["min"] 
                age_score = self.scoring_func(cv["info_age"]-pivot, 1.5, -2)
        except Exception as e:
            logger.warning("age_score=0. Error in calculating age score: {}".format(e))
            age_score = 0
        return age_score

    def scoring_gender(self, cv):
        try:
            gender_score = 0
            if cv["info_gender"] == self.filter_dict["req_gender"]["gender"]:
                gender_score = 1
        except Exception as e:
            logger.warning("gender_score=0. Error in calculating gender score: {}".format(e))
            gender_score = 0
        return gender_score
    
    def scoring_skills(self, candidate_skills):
        try:
            required_skills = self.filter_dict["req_skills"]["skills"]

            matched_cnt = 0
            for skill in required_skills:
                if skill in candidate_skills:
                    matched_cnt += 1
            score_1 = matched_cnt / len(required_skills)

            concat_required_skills = " ".join(["Experience " + skill for skill in required_skills])
            required_skills_feature = self.get_phobert_embedding(concat_required_skills)
            candidate_skills_feature = self.get_phobert_embedding(candidate_skills)
            score_2 = F.cosine_similarity(required_skills_feature, candidate_skills_feature).item()
        except Exception as e:
            logger.warning("skill_score=0. Error in calculating skill score: {}".format(e))
            score_1 = 0
            score_2 = 0
        return score_1 * 0.5 + score_2 * 0.5

    def scoring_seniority(self, experiences):
        try:
            required_senority = "{} at {}".format(self.filter_dict["req_seniority"]["seniority"],
                                                    self.filter_dict["req_position"]["position"]) 
            required_senority_features = self.get_phobert_embedding(required_senority)

            matched_cnt = 0
            senority_score = 0
            for idx, exp in enumerate(experiences):
                exp_senority = "{} experienced at {}".format(exp["total_time"], exp["exp_position"])
                exp_senority_features = self.get_phobert_embedding(exp_senority)
                score = 1/(idx+1) * F.cosine_similarity(required_senority_features, exp_senority_features).item()
                senority_score += score
                matched_cnt += 1/(idx+1)
            senority_score = senority_score / matched_cnt if matched_cnt > 0 else 0
        except Exception as e:
            logger.warning("senority_score=0. Error in calculating senority score: {}".format(e))
            senority_score = 0
        return senority_score

    def calculate_single_cv(self, cv):
        skill_score = self.scoring_skills(cv["others_skills"])
        seniority_score = self.scoring_seniority(cv["experience"])
        age_score = self.scoring_age(cv)
        gender_score = self.scoring_gender(cv)

        total_score = 0
        with ignored(Exception): total_score = skill_score * self.weights["req_skills"]
        with ignored(Exception): total_score += seniority_score * self.weights["req_seniority"]
        with ignored(Exception): total_score += age_score * self.weights["req_age"]
        with ignored(Exception): total_score += gender_score * self.weights["req_gender"]

        return total_score

    def rank(self, cv_list):
        score_list = []
        for cv in tqdm(cv_list, desc="Analyzing..."):
            score_list.append(self.calculate_single_cv(cv))
        
        # cv_list_with_score = zip(cv_list, score_list)
        # cv_list_with_score = sorted(cv_list_with_score, key=lambda x: x[1], reverse=True)
        # return cv_list_with_score
        return score_list


# def parallel_rank(cv_list):
#     score_list = []
#     import ipdb; ipdb.set_trace()
#     pool = multiprocessing.Pool(num_workers)
#     output = list(tqdm(
#             pool.imap(self.calculate_single_cv, cv_list), total=len(cv_list), desc="Analyzing...")
#         )
#     pool.terminate()
    
#     cv_list_with_score = zip(cv_list, score_list)
#     cv_list_with_score = sorted(cv_list_with_score, key=lambda x: x[1], reverse=True)
#     return cv_list_with_score


class ITRanker(BaseRanker):
    def __init__(self, filter_dict: dict, device: str):
        super().__init__(filter_dict, device)
    
    def scoring_exp_company(self, companies):
        try:
            required_company = self.filter_dict["req_company"]["company"]
            required_company_features = []
            for company in required_company:
                required_company_features.append(self.get_phobert_embedding(company))
            required_company_features = torch.stack(required_company_features)
            
            candidate_company_features = []
            for company in companies:
                candidate_company_features.append(
                    self.get_phobert_embedding(company["exp_company_name"]))
            candidate_company_features = torch.stack(candidate_company_features)

            company_score_matrix = torch.zeros(len(required_company), len(companies))
            for i, req in enumerate(required_company_features):
                for j, cand in enumerate(candidate_company_features):
                    company_score_matrix[i, j] = F.cosine_similarity(req, cand).item()
            company_score = torch.norm(company_score_matrix).item() / math.sqrt((len(required_company) * len(companies)))
        except Exception as e:
            logger.warning("company_score=0. Error in calculating company score: {}".format(e))
            company_score = 0
        return company_score

    def scoring_university(self, universities):
        try:
            required_universities = self.filter_dict["req_university"]["university"]
            required_university_features = []
            for university in required_universities:
                required_university_features.append(self.get_phobert_embedding(university))
            required_university_features = torch.stack(required_university_features)
            
            candidate_university_features = []
            for university in universities:
                candidate_university_features.append(
                    self.get_phobert_embedding(university["edu_school_univ"]))
            candidate_university_features = torch.stack(candidate_university_features)

            university_score_matrix = torch.zeros(len(required_universities), len(universities))
            for i, req in enumerate(required_university_features):
                for j, cand in enumerate(candidate_university_features):
                    university_score_matrix[i, j] = F.cosine_similarity(req, cand).item()
            university_score = torch.norm(university_score_matrix).item() / math.sqrt((len(required_universities) * len(universities)))
        except Exception as e:
            logging.warning("university_score=0. Error in scoring_university: {}".format(e))
            university_score = 0
        return university_score

    def calculate_single_cv(self, cv):
        company_score = self.scoring_exp_company(cv["experience"])
        university_score = self.scoring_university(cv["education"])
        skill_score = self.scoring_skills(cv["others_skills"])
        seniority_score = self.scoring_seniority(cv["experience"])
        age_score = self.scoring_age(cv)
        gender_score = self.scoring_gender(cv)

        total_score = 0
        with ignored(Exception): total_score += skill_score * self.weights["req_skills"]
        with ignored(Exception): total_score += seniority_score * self.weights["req_seniority"]
        with ignored(Exception): total_score += age_score * self.weights["req_age"]
        with ignored(Exception): total_score += gender_score * self.weights["req_gender"]
        with ignored(Exception): total_score += company_score * self.weights["req_company"]
        with ignored(Exception): total_score += university_score * self.weights["req_university"]
        return total_score


class SaleRanker(BaseRanker):
    def __init__(self, filter_dict: dict, device: str):
        super().__init__(filter_dict, device)

    def scoring_height(self, height):
        try:
            height_score = 1
            if height not in range(self.filter_dict["req_height"]["min"], self.filter_dict["req_height"]["max"]):
                pivot = self.filter_dict["req_height"]["max"] \
                                if height > self.filter_dict["req_height"]["max"] \
                                else self.filter_dict["req_height"]["min"] 
                height_score = self.scoring_func(height-pivot, 2, -2)
        except Exception as e:
            logger.warning("height_score=0. Error in calculating height score: {}".format(e))
            height_score = 0
        return height_score

    def scoring_bodymass(self, bodymass):
        try:
            bodymass_score = 1
            if bodymass not in range(self.filter_dict["req_bodymass"]["min"], self.filter_dict["req_bodymass"]["max"]):
                pivot = self.filter_dict["req_body"]["max"] \
                                if bodymass > self.filter_dict["req_bodymass"]["max"] \
                                else self.filter_dict["req_bodymass"]["min"] 
                bodymass_score = self.scoring_func(bodymass-pivot, 2, -2)
        except Exception as e:
            logger.warning("bodymass_score=0. Error in calculating bodymass score: {}".format(e))
            bodymass_score = 0
        return bodymass_score

    def scoring_office_location_and_travel_time(self, office_location_list, travel_time_list):
        try:
            required_office_location = self.filter_dict["req_office_location"]["office_location"]
            required_travel_time = self.filter_dict["req_travel_time"]["travel_time"]

            required_office_location_and_travel_time_features = []
            for time, location in zip(required_office_location, required_travel_time):
                required_office_location_and_travel_time_features.append(
                    self.get_phobert_embedding(f"Take about {time} minutes to travel to {location}"))

            candidate_office_location_and_travel_time_features = []
            for travel_time, office_location in zip(travel_time_list, office_location_list):
                candidate_office_location_and_travel_time_features.append(
                    self.get_phobert_embedding(f"Take about {travel_time} minutes to travel to {office_location}"))

            office_location_and_travel_time_score_matrix = torch.zeros(len(required_office_location_and_travel_time_features), 
                                                                        len(candidate_office_location_and_travel_time_features))
            for i, req in enumerate(required_office_location_and_travel_time_features):
                for j, cand in enumerate(candidate_office_location_and_travel_time_features):
                    office_location_and_travel_time_score_matrix[i, j] = F.cosine_similarity(req, cand).item()
            
            office_location_and_travel_time_score = torch.norm(office_location_and_travel_time_score_matrix).item() \
                / math.sqrt((len(required_office_location_and_travel_time_features) * len(candidate_office_location_and_travel_time_features)))
        except Exception as e:
            logger.warning("office_location_and_travel_time_score=0. Error in scoring_office_location_and_travel_time: {}".format(e))
            office_location_and_travel_time_score = 0
        return office_location_and_travel_time_score

    def scoring_shift_work(self, shift_work):
        try:
            shift_work_score = 0
            if shift_work == self.filter_dict["req_shift_work"]["shift_work"]:
                shift_work_score = 1
        except Exception as e:
            logger.warning("shift_work_score=0. Error in calculating shift_work score: {}".format(e))
            shift_work_score = 0
        return shift_work_score

    def calculate_single_cv(self, cv):
        height_score = self.scoring_height(cv["req_height"])
        bodymass_score = self.scoring_bodymass(cv["req_bodymass"])
        skill_score = self.scoring_skills(cv["others_skills"])
        seniority_score = self.scoring_seniority(cv["experience"])
        age_score = self.scoring_age(cv)
        gender_score = self.scoring_gender(cv)
        shift_work_score = self.scoring_shift_work(cv["shift_work"])
        office_location_and_travel_time_score = self.scoring_office_location_and_travel_time(
                                                    cv["office_location"], cv["travel_time"])

        total_score = 0
        with ignored(Exception): total_score += skill_score * self.weights["req_skills"]
        with ignored(Exception): total_score += seniority_score * self.weights["req_seniority"]
        with ignored(Exception): total_score += age_score * self.weights["req_age"]
        with ignored(Exception): total_score += gender_score * self.weights["req_gender"]
        with ignored(Exception): total_score += height_score * self.weights["req_height"]
        with ignored(Exception): total_score += bodymass_score * self.weights["req_bodymass"]
        with ignored(Exception): total_score += shift_work_score * self.weights["req_shift_work"]
        with ignored(Exception):
            average_weight = (self.weights["req_office_location"] + self.weights["req_travel_time"]) / 2
            total_score += office_location_and_travel_time_score * average_weight
        return total_score