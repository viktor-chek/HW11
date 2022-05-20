import json


def load_candidates_from_json(candidates):
    """Читает json, возвращает список"""
    with open(candidates, encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate(data, candidate_id):
    """Возвращает одного кандидата по его id"""
    for item in data:
        if item["id"] == candidate_id:
            return item


def get_candidates_by_name(data, candidate_name):
    """Возвращает кандидатов по имени"""
    result = []
    for item in data:
        if candidate_name.title() in item["name"]:
            result.append(item)
    return result


def get_candidates_by_skill(data, skill_name):
    """Возвращает кандидатов по навыку"""
    result = []
    for item in data:
        if skill_name in item["skills"].lower().split(", "):
            result.append(item)
    return result
