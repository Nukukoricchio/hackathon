import io

from django.shortcuts import get_object_or_404
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Candidate, CvFile
from .extractors import extract
from .base64_to_img import decode_design_image
from .preprocessing import preprocessing


def process_cv(file):
	extract_info = extract(file)
	extract_info = preprocessing(extract_info)
	info_email = extract_info.get('info_email', '')
	info_picture = extract_info.get('info_picture', '')
	info_name = extract_info.get('info_name', '')
	info_birthdate = extract_info.get('info_birthdate', '')
	info_gender = extract_info.get('info_gender', '')
	info_phone = extract_info.get('info_phone', '')
	info_location_1 = extract_info.get('info_location_1', '')
	info_location_2 = extract_info.get('info_location_2', '')
	exp_period = extract_info.get('exp_period', '')
	exp_company_name = extract_info.get('exp_company_name', '')
	experience = extract_info.get('experience', '')
	exp_confident = extract_info.get('exp_confident', '')
	edu_school_univ = extract_info.get('edu_school_univ', '')
	edu_major = extract_info.get('edu_major', '')
	education = extract_info.get('education', '')
	others_education = extract_info.get('others_education', '')
	others_career_objective = extract_info.get('others_career_objective', '')
	others_skills = extract_info.get('others_skills', '')
	others_profile = extract_info.get('others_profile', '')
	info_normalized_birthdate = extract_info.get('info_normalized_birthdate', '')
	if info_email:
		try:
			candidate = Candidate.objects.get(info_email=info_email)
		except Candidate.DoesNotExist:
			candidate = Candidate.objects.create(info_email=info_email)
		if info_picture:
			img = decode_design_image(info_picture)
			img_io = io.BytesIO()
			img.save(img_io, format='JPEG')
			candidate.info_picture = InMemoryUploadedFile(img_io,
				field_name=None, name=info_email+".jpg",
				content_type='image/jpeg',
				size=img_io.tell,
				charset=None
			)
		candidate.info_name = info_name
		candidate.info_birthdate = info_birthdate
		candidate.info_gender = info_gender
		candidate.info_phone = info_phone
		candidate.info_location_1 = info_location_1
		candidate.info_location_2 = info_location_2
		candidate.exp_period = exp_period
		candidate.exp_company_name = exp_company_name
		candidate.experience = experience
		candidate.exp_confident = exp_confident
		candidate.edu_school_univ = edu_school_univ
		candidate.edu_major = edu_major
		candidate.education = education
		candidate.others_education = others_education
		candidate.others_career_objective = others_career_objective
		candidate.others_skills = others_skills
		candidate.others_profile = others_profile
		candidate.info_normalized_birthdate = info_normalized_birthdate

		candidate.content = extract_info
		# Save candidate
		candidate.save()
		# New file
		cv_file = CvFile(file=file)
		cv_file.candidate = candidate
		cv_file.save()

		print('Doneee')
		return candidate

	return 
	    

