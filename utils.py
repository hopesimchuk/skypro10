import json


# '''Функция которая загрузит данные из файла'''


def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


# '''Функция которая покажет всех кандидатов'''


def format_candidates(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    candidates = load_json()
    # Начинаем форматирование вывода(чтобы в начале и в конуе было <pre>)
    result = '<pre>'
    # Так как candidates список со словарем, то мы можем пройтись по нему циклом
    for candidate in candidates:
        result += f"""
               {candidate["name"]}\n
               {candidate["position"]}\n
               {candidate["skills"]}\n
           """
    # Добавляем в конце к строке pre'''
    result += '</pre>'
    return result


def get_all_candidates() -> list[dict]:
    return load_json()


# '''Функция которая выведет кандидатов по айди'''


def get_candidate_by_id(uid: int):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


# '''Функция которая ищет кандидатов по скилу'''


def get_candidate_by_skill(skill: str) -> list[dict]:
    # можем передавать список со словарем так как один и тот же скил может быть у неск кандидатов
    candidates = get_all_candidates()
    for candidate in candidates:
        # исп сплит так как навыки указаны через запятую
        if skill in candidate['skills'].lower().split(', '):
            # если скил есть у кандидата то добавляем кандидата в список
            result.append(candidate)
    return result
