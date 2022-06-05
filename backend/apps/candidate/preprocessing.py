"""
TODO: + Field Normalization
      + 

"""
from datetime import datetime, date
import re



def validate_phone(phone: str):
    validate_phone_pattern = "^(03|05|07|08|09|01[2|6|8|9])([0-9]{8})$"
    if re.match(validate_phone_pattern, phone):
        return phone
    return ""     # "Can't Extracted"

def validate_name():
    ...

def norm_name(name):
    return name.title()

def norm_university():
    ...

def norm_company():
    ...

def norm_birthdate(text):
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    return ""

def diff_month(d1, d2):
    d1 = datetime.strptime(d1, "%m/%Y")
    d2 = datetime.strptime(d2, "%m/%Y")
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# def norm_skills(skills):

def validate_gender(gender):
    lower_gender = gender.lower()
    valid_gender = ["male", "female", "nam", "nữ", "nu"]
    if lower_gender not in valid_gender:
        return ""
    return gender

def norm_gender(gender):
    gender = gender.lower()
    norm_dict = {
        "male": ["nam", "male"],
        "female": ["female", "nữ", "nu"]
    }
    for k, v in norm_dict.items():
        if gender in v:
            return k
    return ""


def preprocessing(json_file: dict):
    json_file["info_phone"] = validate_phone(json_file["info_phone"])
    try:
        json_file["info_birthdate"] = norm_birthdate(json_file["info_birthdate"])
        json_file["info_age"] = ""
        if json_file["info_birthdate"]:
            json_file["info_age"] = age(json_file["info_birthdate"])
        json_file["info_birthdate"] = json_file["info_birthdate"].strftime("%d/%m/%Y")
    except:
        pass
    json_file["info_gender"] = norm_gender(validate_gender(json_file["info_gender"]))
    json_file["info_name"] = norm_name(json_file["info_name"])

    for idx, exp in enumerate(json_file["experience"]):
        try:
            start_time = json_file["experience"][idx]["normalized_period"]["start"]
            end_time = json_file["experience"][idx]["normalized_period"]["end"]
            json_file["experience"][idx]["total_time"] = diff_month(end_time, start_time)
        except:
            json_file["experience"][idx]["total_time"] = ""
    
    return json_file