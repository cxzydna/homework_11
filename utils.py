import json


def load_candidates_from_json():
    """
    The function loads data from a JSON file
    :return:     - a list of candidates
    """
    with open("candidates.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_candidate_by_id(candidate_id, data):
    """
    The function returns the candidate by his id
    :param candidate_id:  - the id of the candidate
    :param data:          - a list of candidates
    :return:              - candidate
    """
    for candidate in data:
        if candidate["id"] == candidate_id:
            return candidate
        else:
            continue


def get_candidates_by_name(candidate_name, data):
    """
    The function returns the candidate by his name
    :param candidate_name:  - the name of the candidate
    :param data:            - a list of candidates
    :return:                - candidates with this name
    """
    result = []
    for candidate in data:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidate_by_skill(skill_name, data):
    """
    The function returns candidates by their skills
    :param skill_name: - skill name
    :param data:       - a list of candidates
    :return:           - a list of candidates with the required skill
    """
    result = []
    for candidate in data:
        if skill_name in candidate["skills"]:
            result.append(candidate)
    return result
