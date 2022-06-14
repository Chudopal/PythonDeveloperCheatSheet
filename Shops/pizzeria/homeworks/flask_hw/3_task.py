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
from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)


class ScheduleStorage:

    def __init__(self, file_path: str, data_path: tuple, datetime_pattern: str) -> None:
        self.file_path = file_path
        self.data_path = data_path
        self.datetime_pattern = datetime_pattern
        self.data = self._convert_data(self._get_data(self._read_file()))

    def _read_file(self) -> dict:
        with open(self.file_path, encoding='utf-8') as file:
            base_data = json.load(file)
        return base_data

    def _get_data(self, base_data) -> dict:
        result = base_data
        for step in self.data_path:
            result = result.get(step)
        return result

    def get_data(self) -> dict:
        return self.data

    def _convert_data(self, data: dict) -> dict:
        for week_day in data.values():
            for task in week_day:
                task["begin_time"] = datetime.strptime(task["begin_time"], self.datetime_pattern)
                task["end_time"] = datetime.strptime(task["end_time"], self.datetime_pattern)
        return data

    def filter_by(self, week_day: str, date: str = None):
        result = self.data.get(week_day)
        if date:
            date = datetime.strptime(date, "%d-%m-%Y")
            result = filter(
                lambda task: task.get('begin_time').date() == date.date(),
                result
            )
        return result


schedule_storage = ScheduleStorage("storage.json", ("3_task", "schedule"), "%d-%m-%Y, %H:%M:%S")


@app.route("/schedule/<string:week_day>/<string:date>")
def get_schedule(week_day, date):
    date_header = f"{week_day}, {date}"
    data = schedule_storage.filter_by(week_day=week_day, date=date)
    return render_template("3_task/schedule.html", data=data, date=date_header)


@app.route("/schedule/<string:week_day>/")
def get_concrete_day_schedule(week_day):
    data = schedule_storage.filter_by(week_day=week_day)
    return render_template("3_task/schedule.html", data=data, date=week_day)


app.run(port=5000, debug=True)
