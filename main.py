from flask import Flask

from utils import format_candidates
from utils import get_all_candidates
from utils import get_candidate_by_id
from utils import get_candidate_by_skill

'''
Шаг 1
Создайте представление для роута `/` (главная страница).
Выведите список в таком формате (тег <pre> - преформатирование)

Для выполнения этого шага создаем функции def load_json и def formate_candidates
'''
app = Flask(__name__)


@app.route('/')
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all_candidates()
    result = format_candidates(candidates)
    return result


'''
Шаг 2
Создайте представление для роута `candidates/<x>`,
Который бы выводил данные кандидата так:
<img src="(ссылка на картинку)">
<pre>
 Имя кандидата -
 Позиция кандидата
 Навыки через запятую
</pre>

Для выполнения этого шага создаем функции def get_all_candidates и def get_candidate_by_id
'''


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Список кандидатов по айди"""
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate[picture]}">'
    # кладем функцию в список чтобы корректно работала, так как здесь принимаем словарь
    result += format_candidates([candidate])
    return result


'''
Шаг 3
Создайте представление `/skills/<x>` для поиска по навыкам.
Выведите тех кандидатов, в списке навыков у которых содержится `skill`.
Поиск по навыку не должен зависеть от регистра.
Для выполнения этого шага создаем функции def get_candidate_by_skill
'''


@app.route('/skills/<skill>')
def page_skills(skill):
    """Поиск по навыку"""
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    # результат форматированная строка
    result = formate_candidates(candidates)
    return result


app.run()
