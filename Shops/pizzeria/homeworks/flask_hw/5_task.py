"""
Измените данную программу для веба
Запросы на фильтрацию данных сделайте через request.args

Ссылки для помощи:
https://docs-python.ru/packages/veb-frejmvork-flask-python/funktsija-make-response/
"""

import json
from typing import List
from typing import Dict
from dataclasses import dataclass
from typing import Protocol
from flask import Flask, request, render_template, jsonify


class Storage(Protocol):

    def get_employees(self, **params) -> 'Employee':
        """Returns employees by passed params"""


class IO(Protocol):

    def make_response(self, employees: List['Employee']) -> None:
        """Returns data from system"""

    def get_data(self) -> Dict[str, str]:
        """Receive data from environment"""


@dataclass
class Employee:
    department: str
    name: str
    role: str
    id: str


class EmployeeStorage:

    def __init__(self, file_path: str, data_path: List) -> None:
        self.file_path = file_path
        self.data_path = data_path
        self.data = self._get_data()

    def _get_data(self) -> Dict:
        base_data = self._read_file()
        return self._extract_data(base_data)

    def _read_file(self) -> Dict:
        with open(self.file_path) as file:
            data = json.load(file)
        return data

    def _extract_data(self, data: Dict) -> Dict:
        result = data
        for step in self.data_path:
            result = result.get(step, {})
        return result

    def get_employees(self, **params) -> List[Employee]:
        result = self.data
        for key, value in params.items():
            if value:
                result = list(filter(
                    lambda item: str(item.get(key)).lower() == str(value),
                    result
                ))
        return list(map(lambda data: Employee(**data), result))


class Console:

    def __init__(self, input_message: str, output_template: str) -> None:
        self.input_message = input_message
        self.output_template = output_template

    def make_response(self, employees: List[Employee]) -> None:
        print(
            "\n".join([self.output_template.format(
                **employee.__dict__
            ) for employee in employees
            ])
        )

    def get_data(self) -> Dict[str, str]:
        base_params = input(self.input_message).split(",")
        return dict(
            list(map(
                lambda param: param.lower().replace(" ", "").split("="),
                base_params
            ))
        )

    def make_error(self, message) -> None:
        print(message)


class EmployeeService:

    def __init__(self, storage: Storage, io: IO, allowed_params: List[str], error_message=None) -> None:
        self.storage = storage
        self.allowed_params = allowed_params
        self.error_message = error_message
        self.io = io

    def get_employees(self):
        params = self.io.get_data()
        valid = self._is_params_valid(params)
        if valid:
            data = self.storage.get_employees(**params)
            self.io.make_response(data)
        else:
            self.io.make_error(self.error_message)

    def _is_params_valid(self, params) -> bool:
        result = True
        if set(params.keys()) - set(self.allowed_params):
            result = False
        return result


class EmployeeWebService(EmployeeService):
    def __init__(self, storage: Storage, allowed_params: List[str], io: IO = None, error_message=None) -> None:
        EmployeeService.__init__(self, storage, io, allowed_params, error_message)

    def get_employees(self, **params):
        valid = self._is_params_valid(params)
        if valid:
            data = self.storage.get_employees(**params)
        else:
            data = {"error": self.error_message}
        return data


if __name__ == "__main__":
    allowed_params = ["name", "department", "id", "role"]
    storage = EmployeeStorage(file_path="storage.json", data_path=["5_task", "employees"])
    employee_service = EmployeeWebService(
        allowed_params=allowed_params,
        storage=storage,
        error_message='Вы ввели неправильный параметр')

    app = Flask(__name__)


    @app.route("/")
    def index():
        employees = employee_service.get_employees(**request.args)
        print(employees)
        return render_template("5_task/employee_service.html", employees=employees)


    app.run()
