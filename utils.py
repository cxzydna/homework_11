import json


def load_candidates_from_json():
    with open("candidates.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_candidate_by_id(candidate_id, data):
    for candidate in data:
        if candidate["id"] == candidate_id:
            return candidate
        else:
            continue


def get_candidates_by_name(candidate_name, data):
    result = []
    for candidate in data:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidate_by_skill(skill_name, data):
    result = []
    for candidate in data:
        if skill_name in candidate["skills"]:
            result.append(candidate)
    return result
