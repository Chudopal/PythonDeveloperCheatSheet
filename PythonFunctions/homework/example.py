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
"""По сути это слой-адаптер, позволяющий не думать о том, как конкретно
хранятся данные в системе, а просто брать их и использовать в
бизнес-логике. Позволяет избежать жесткой привязки к формату и способу
хранения. При изменении способа хранения, нужно будет периписать только
этот блок а не всю систему."""

def get_vacancy_storage_from_list() -> List[Dict]:
    return VACANCIES


def get_users_storage_from_dict() -> Dict:
    return USERS_CV


def add_vacancy_to_user_list(vacancy: Dict) -> None:
    USERS_VACANCIES.append(vacancy)


def update_cv_from_dict(cv: Dict) -> None:
    USERS_CV.update(cv)


def get_vacancies_by_salary_from_list(salary: int) -> List[Dict]:
    
    def filter_salary(vacancy: Dict) -> bool:
        max_salary = vacancy.get("salary", {}).get("max")
        min_salary = vacancy.get("salary", {}).get("min")
        return min_salary <= salary <= max_salary

    return list(
        filter(filter_salary, get_vacancy_storage_from_list())
    )


def get_vacancies_by_location_from_list(location: str) -> List[Dict]:
    return list(
        filter(
            lambda vacancy: location == vacancy.get("location"),
            get_vacancy_storage_from_list()
        )
    )


def get_vacancies_by_skills_from_list(
    skills: List[str],
    match_skills_number: int
) -> List[Dict]:
    
    def filter_by_skills(vacancy):
        return len(
            set(map(lambda skill: skill.lower().replace(" ", ""),
                vacancy.get("skills"))) & set(skills)
        ) >= match_skills_number
    
    return list(
        filter(filter_by_skills, get_vacancy_storage_from_list())
    )


def get_vacancy_by_id_from_list(vacancy_id: int) -> Dict:
    vacancies = get_vacancy_storage_from_list()
    return next((vacancy for vacancy in vacancies
        if vacancy.get("id") == vacancy_id))


def get_user_skills_from_dict() -> List:
    return get_users_storage_from_dict().get("skills")


def get_user_salary_from_dict() -> int:
    return get_users_storage_from_dict().get("salary")


def get_user_location_from_dict() -> str:
    return get_users_storage_from_dict().get("location")


################    ################    ################    ################
# DOMAIN LAYER #    # DOMAIN LAYER #    # DOMAIN LAYER #    # DOMAIN LAYER #
################    ################    ################    ################
"""Слой который содержит основную логику приложения. Важно, чтобы функции в
нем были максимально раздроблены, максимально малы. Это позволит потом их
множество раз переиспользовать в других слоях. Слой домена не зависит больше
ни от чего, кроме самих функций в этом же домене."""


def add_cv_action(cv: Dict, add_cv_func: Callable[[Dict], None]):
    add_cv_func(cv)


def get_relevant_salary_vacancies(
    get_user_salary: Callable[[], int],
    get_vacancies_by_salary: Callable[[int], List[Dict]],
) -> List[Dict]:
    user_salary = get_user_salary()
    return get_vacancies_by_salary(user_salary)


def get_relevant_location_vacancies(
        get_user_location: Callable[[], str],
        get_vacancies_by_location: Callable[[int], List[Dict]],
    ) -> List[Dict]:
    user_location = get_user_location()
    return get_vacancies_by_location(user_location)


def get_relevant_skills_vacancies(
    match_skills_number: int,
    get_user_skills: Callable[[], List[str]],
    get_vacancies_by_skills: Callable[[List[str]], List[Dict]]
) -> List[Dict]:
    user_skills = get_user_skills()
    return get_vacancies_by_skills(user_skills, match_skills_number)


def map_ids_and_vacancies(
    id_list: List[int],
    vacancy_list: List[Dict]
) -> List[Dict]:
    vacancies = []
    for vacancy_id in id_list:
        vacancies.append(
            next((vacancy for vacancy in vacancy_list
                if vacancy.get("id") == vacancy_id))
        )
    return vacancies


def merge_vacancies(
    *vacancies_lists: List[List[Dict]],
    match_coefficient: int
) -> List[Dict]:

    full_vacancies_list = list(sum(vacancies_lists, []))
    merged_vacancies = []

    for vacancy in full_vacancies_list:
        if full_vacancies_list.count(vacancy) >= match_coefficient:
            merged_vacancies.append(vacancy)
            full_vacancies_list = list(filter(
                lambda x: x != vacancy,
                full_vacancies_list
            ))

    return merged_vacancies



def apply_for_a_job(
    vacancy_id: int,
    get_vacancy_by_id: Callable[[int], Dict],
    assign_vacancy_to_user: Callable[[Dict], None]
) -> None:
    vacancy: Dict = get_vacancy_by_id(vacancy_id)
    assign_vacancy_to_user(vacancy)


########################### ########################### ########################### 
# CONSOLE INTERFACE LAYER # # CONSOLE INTERFACE LAYER # # CONSOLE INTERFACE LAYER # 
########################### ########################### ########################### 
"""Здесь находятся все, что связано с путем вывода программы. В данный момент, это
только консоль, но если это будет телеграм бот или веб-приложение, мы должны изменить
только этот слой. Здесь можно привязаться к формату данных, потому что эти данные
будут получены из слоя безнес-логики, а значит в их структуре можно быть уверенным."""

# Функции работы со строками, форматирующие функции и функции кастомизации интерфейса

def format_items(
    actions: Dict[int, str],
    sep: str = ". ",
    sep_item: str = ";\n",
    end: str = ".\n"
) -> str:
    return f"{sep_item}".join([
        "{}{}{}".format(
            number, sep, action
        ) for number, action in actions.items()
    ]) + end


def get_menu_items():
    return {
        1: "Добавить резюме",
        2: "Просмотр всех вакансий",
        3: "Просмотр релевантных вакансий",
        4: "Откликнуться на вакансию",
        5: "Выход"
    }


def cast_vacancy_to_str(vacancy: Dict) -> str:
    return ("Позиция \"{position}\"\n\t" +
        "Зарплата: {min_salary}-{max_salary}\n\t" +
        "Локация: {location}\n\tКомпания {company_name}\n\t" +
        "Навыки: {real_skills}").format(
            **vacancy,
            min_salary=vacancy.get("salary", {}).get("min"),
            max_salary=vacancy.get("salary", {}).get("max"),
            real_skills=", ".join(vacancy.get("skills"))
        )


def format_vacancies_short(vacancies: Dict) -> Dict[int, str]:
    return {
        vacancy.get("id"): vacancy.get("position")
        for vacancy in vacancies
    }


def format_vacancies(vacancies: List[Dict]):
    return {
        vacancy.get("id"): cast_vacancy_to_str(vacancy)
        for vacancy in vacancies
    }


def get_cv_form():
    return {
        "name": "\tВведите свое имя: ",
        "location": "\tВведите свою локацию: ",
        "skills": "\tВведите через запятую свои навыки: ",
        "salary": "\tНапишите желаемую зарплату: ",
    }


def get_phrase(key: str) -> Dict[str,str]:
    phrases = {
        "choice": "Введите номер пункта меню: ",
        "vacancy_id": "Введите номер вакансии: ",
        "continue": "Чтобы продолжить нажмите Enter.",
    }
    return {key: phrases.get(key)}


# Блок валидаторов

def validate_user_cv(raw_user_cv: Dict) -> Dict:
    return {
        "name": raw_user_cv.get("name", ""),
        "location": raw_user_cv.get("location", ""),
        "skills": list(map(lambda skill: skill.lower(), # очистка от пробелов и разбиение строки на список
            raw_user_cv.get("skills").replace(" ", "").split(","))),
        "salary": int(raw_user_cv.get("salary", 0))
    }


def validate_user_choice(choice: Dict) -> Dict:
    return {
        "choice": int(choice.get("choice"))
    }


def validate_vacancies(vacancies: Dict) -> str:
    if not vacancies:
        result = "Для вас нет подходящих вакансий =(\n"
    else:
        result = format_items(vacancies)

    return result


def validate_vacancy_number(vacancy_id):
    return int(vacancy_id)


# Привязка к консоли

def execute_console_output(*output_list: List) -> None:
    for output in output_list:
        print(output, end="", sep="")


def execute_console_input(**input_items: Dict) -> any:
    return {
        key: input(form)
        for key, form in input_items.items()
    }


#####################   #####################   #####################
# CONTROLLERS LAYER #   # CONTROLLERS LAYER #   # CONTROLLERS LAYER #
#####################   #####################   #####################
"""Слой, в котором происходи связь интерфейса(консоли), логики и хранилища
контроллер сразу зависит от всех слоев, потому функции могут быть в нем больше,
и зависеть от того, что отдают другие слои. Этот слой меняется чаще всех остальных."""


def menu_controller() -> Dict:
    menu = format_items(get_menu_items())
    execute_console_output(menu)
    raw_choice = execute_console_input(
        **get_phrase("choice")
    )
    return validate_user_choice(
        raw_choice
    )


def add_cv_controller() -> None:
    form = get_cv_form()
    raw_user_info = execute_console_input(**form)
    clean_user_info = validate_user_cv(raw_user_cv=raw_user_info)
    add_cv_action(clean_user_info, update_cv_from_dict)


def get_all_vacancies_controller() -> None:
    vacancies = get_vacancy_storage_from_list()
    execute_console_output(
        validate_vacancies(format_vacancies(vacancies))
    )


def get_lists_of_vacancies(match_coefficient):
    return [ 
        get_relevant_skills_vacancies(
            match_coefficient,
            get_user_skills_from_dict,
            get_vacancies_by_skills_from_list
        ),
        get_relevant_salary_vacancies(
            get_user_salary_from_dict,
            get_vacancies_by_salary_from_list
        ),
        get_relevant_location_vacancies(
            get_user_location_from_dict,
            get_vacancies_by_location_from_list
        ),
    ]


def get_relevant_vacancies() -> None:
    match_coefficient = 2
    common_vacancies = get_lists_of_vacancies(match_coefficient)
    relevant_vacancies = merge_vacancies(
        *common_vacancies,
        match_coefficient=match_coefficient
    )
    return relevant_vacancies


def relevant_vacancies_controller() -> None:

    relevant_vacancies = get_relevant_vacancies()

    execute_console_output(
        validate_vacancies(format_vacancies(relevant_vacancies))
    )


def apply_for_a_job_controller() -> None:
    relevant_vacancies = get_relevant_vacancies()

    execute_console_output(
        validate_vacancies(format_vacancies_short(relevant_vacancies))
    )

    form = get_phrase("vacancy_id")
    vacancy_id = validate_vacancy_number(
        **execute_console_input(**form)
    )
    apply_for_a_job(
        vacancy_id,
        get_vacancy_by_id_from_list,
        add_vacancy_to_user_list
    )


def get_choices() -> Dict[int, Callable]:
    return {
        1: add_cv_controller,
        2: get_all_vacancies_controller,
        3: relevant_vacancies_controller,
        4: apply_for_a_job_controller,
        5: quit
    }


def execute_choice(choice: int) -> None:
    choices = get_choices()
    choices.get(
        choice
    )()
    execute_console_input(**get_phrase("continue"))


def run():
    while True:
        choice = menu_controller()
        execute_choice(**choice)

run()
