"""Программа для подбора вакансий.
Позволяет пользователю подбирать вакансию.
Возможности пользователя:
- добавление резюме
- просмотр релевантных вакансий
- отклик на вакансию
Релевантной вакансией считается вакансия,
в под которую подходит хотя бы 2 навыка
пользователя, совпадают ожидания по
зарплате и локация.
"""

from typing import Dict, List, Callable

############    ############    ############    ############    ############
# STORAGES #    # STORAGES #    # STORAGES #    # STORAGES #    # STORAGES #
############    ############    ############    ############    ############
"""Представляет собой сырые данные системы, это может быть словарь, список
или другая структура данных. Может быть файл или база данных. Одним словом -
это то откуда мы берем какие-то данные и куда мы их сохраням. Жесткой привязки
к формату данных и месту их хранения нужно избегать, так как при их изменении
у нас не должно быть необходимости переписывать всю сиситему заново, чтобы
подстроится под новый формат хранения.
"""


VACANCIES = [
    {
        "id": 1,
        "position": "Software Engineer",
        "location": "Minsk",
        "salary": {
            "min": 2000,
            "max": 4000,
        },
        "company_name": "ItechArt-group",
        "skills": [
            "Python", "Django", "Flask",
            "PostgreSQL", "AWS", "NGINX"
        ]
    },
    {
        "id": 2,
        "position": "DevOps Engineer",
        "location": "remote",
        "salary": {
            "min": 1000,
            "max": 5000,
        },
        "company_name": "LeverX-group",
        "skills": [
            "Docker", "Terraform", "Jenkins",
            "Luigi", "CI/CD", "AWS", "k8s"
        ]
    },
    {
        "id": 3,
        "position": "React Developer",
        "location": "remote",
        "salary": {
            "min": 1000,
            "max": 2000,
        },
        "company_name": "Itransition",
        "skills": [
            "React", "Javascript", "Redux"
        ]
    }
]

USERS_CV = {
    "name": "",
    "location": "",
    "skills": [],
    "salary": 0, 
}

USERS_VACANCIES = list()


#####################   #####################   #####################
# DATA ACCESS LAYER #   # DATA ACCESS LAYER #   # DATA ACCESS LAYER #
#####################   #####################   #####################


def filer_salary():
    pass


def get_vacancies_by_salary_from_list(salary: int) -> List[Dict]:
    return list(
        filter(
            lambda vacancy: vacancy.get("salary", {}).get("min") <= salary <= vacancy.get("salary", {}).get("max"),
            VACANCIES
        )
    )


def get_vacancies_by_location_from_list(location: str) -> List[Dict]:
    return list(
        filter(
            lambda vacancy: location == vacancy.get("location"),
            VACANCIES
        )
    )


def get_vacancies_by_skills_from_list(skills: List[str]) -> List[Dict]:
    return list(
        filter(
            lambda vacancy: any(set(vacancy.get("skills")) & set(skills)),
            VACANCIES
        )
    )


def get_vacancy_by_id_from_list(id: int) -> Dict:
    return next(lambda vacancy: vacancy.get("id") == id, VACANCIES)


def add_vacancy_to_user_list(vacancy: Dict) -> None:
    USERS_VACANCIES.append(vacancy)


def get_users_skills_from_dict() -> List:
    USERS_CV.get("skills")


def update_cv_from_dict(cv: Dict) -> None:
    USERS_CV.update(cv)


################    ################    ################    ################
# DOMAIN LAYER #    # DOMAIN LAYER #    # DOMAIN LAYER #    # DOMAIN LAYER #
################    ################    ################    ################


def add_cv_action(cv: Dict, add_cv_func: Callable[[Dict], None]):
    add_cv_func(cv)


def get_relevant_salary_vacancies(
        users_salary: int,
        get_vacancies_by_salary: Callable[[int], List[Dict]],
    ) -> List[Dict]:
        return get_vacancies_by_salary(users_salary)


def get_relevant_location_vacancies(
        users_location: int,
        get_vacancies_by_location: Callable[[int], List[Dict]],
    ) -> List[Dict]:
    return get_vacancies_by_location(users_location)


def get_relevant_skills_vacancies(
        users_skills: List[str],
        get_vacancies_by_skills: Callable[[List[str]], List[Dict]]
    ) -> List[Dict]:
    return get_vacancies_by_skills(users_skills)


def merge_vacancies():
    pass


def apply_for_a_job(
        vacancy_id: int,
        get_vacancy_by_id: Callable[[int], Dict],
        assign_vacancy_to_user: Callable[[Dict], None]
    ) -> None:
        vacancy: Dict = get_vacancy_by_id(vacancy_id)
        assign_vacancy_to_user(vacancy)


######################  ######################  ######################
# PRESENTATION LAYER #  # PRESENTATION LAYER #  # PRESENTATION LAYER #
######################  ######################  ######################


def choose_action_str() -> str:
    actions = [
        "1. Добавить резюме",
        "2. Получить релевантные вакансии",
        "3. Откликнуться на вакансию",
        "4. Выход",
    ]
    return "\n".join(actions)


########################### ########################### ########################### 
# CONSOLE INTERFACE LAYER # # CONSOLE INTERFACE LAYER # # CONSOLE INTERFACE LAYER # 
########################### ########################### ########################### 

...

#####################   #####################   #####################
# CONTROLLERS LAYER #   # CONTROLLERS LAYER #   # CONTROLLERS LAYER #
#####################   #####################   #####################

...