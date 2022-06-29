"""
Небольшое приложение расписания.
Запустите приложение, перейдите на
localhost:5000/schedule/monday/06-06-2022
Посмотрите что будет, поймите как это работает.
Переделайте приложение так, чтобы при переходе на
localhost:5000/schedule/monday/06-06-2022
Выводилось именно расписание на понедельник 6го июня 2022 года
Как работают шаблоны фласк, можно почитать тут:
- https://flask-russian-docs.readthedocs.io/ru/latest/tutorial/templates.html
"""

import json
from typing import List
from typing import Dict
from flask import Flask
from flask import render_template

app = Flask(__name__)


class ScheduleStorage:

    def __init__(self, file_path: str, data_path: tuple) -> None:
        self.file_path = file_path
        self.data_path = data_path
        self.data = self._get_data(self._read_file())

    def _read_file(self) -> Dict:
        with open(self.file_path) as file:
            base_data = json.load(file)
        return base_data

    def _get_data(self, base_data) -> List:
        result = base_data
        for step in self.data_path:
            result = result.get(step)
        return result

    def get_data(self) -> List:
        return self.data


schedule_storage = ScheduleStorage("storage.json", ["3_task", "schedule"])


@app.route("/schedule/<string:week_day>/<string:date>")
def get_schedule(week_day, date):
    date = f"{week_day}, {date}"
    data = schedule_storage.get_data().get('monday')[0].items()
    return render_template("3_task/schedule.html", data=data, date=date)


app.run(port=5000)