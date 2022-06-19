import psycopg2
from psycopg2 import sql
from typing import List
from models import Doctor, Patient, Diagnosis
from uuid import uuid4
from dataclasses import asdict


class DBException(Exception):
    def __str__(self):
        return "Database error occurred"


class DBStorage:
    def __init__(self, **kwargs):
        self._host = kwargs.get('host', '127.0.0.1')
        self._user = kwargs.get('user', '')
        self._password = kwargs.get('password', '')
        self._dbname = kwargs.get('dbname')

    def execute(self, *sql_query: dict) -> psycopg2:
        try:
            connector = psycopg2.connect(host=self._host, user=self._user, password=self._password, dbname=self._dbname)
            cursor = connector.cursor()
            for query in sql_query:
                cursor.execute(**query)
            connector.commit()
            return cursor
        except Exception as error:
            raise DBException(error)

    def get_data(self, table: str, columns: tuple = None, where: dict = None) -> list[dict]:
        sql_query = self._select_query(table, columns, where)
        db_response = self.execute(sql_query)
        columns = [item[0] for item in db_response.description]
        data = [dict(zip(columns, row)) for row in db_response.fetchall()]
        return data

    def add_data(self, table: str, data: dict):
        sql_query = self._insert_query(table, data)
        self.execute(sql_query)

    def _select_query(self, table: str, columns: list = None, where: dict = None) -> psycopg2.sql:
        if columns:
            query = sql.SQL("SELECT {columns} FROM {table}").format(
                table=sql.SQL(table),
                columns=sql.SQL(", ").join([sql.Identifier(col) for col in columns])
            )
        else:
            query = sql.SQL("SELECT * FROM {table}").format(
                table=sql.SQL(table)
            )

        if where:
            query += self._format_where_params(where)
        query += sql.SQL(";")

        return {"query": query, "vars": where}

    def _insert_query(self, table: str, variables: dict) -> psycopg2.sql:
        query = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
            table=sql.SQL(table),
            columns=sql.SQL(", ").join([sql.Identifier(col) for col in variables.keys()]),
            values=sql.SQL(", ").join([sql.Placeholder(val) for val in variables.keys()])
        )
        query += sql.SQL(";")

        return {"query": query, "vars": variables}

    def _format_where_params(self, variables: dict) -> psycopg2.sql:
        return sql.SQL(" WHERE ") + sql.SQL(" AND ").join([sql.SQL("{}={}").format(
            sql.Identifier(identifier), sql.Placeholder(identifier)) for identifier in variables])


class Hospital:

    def __init__(self, storage: DBStorage):
        self.storage = storage

    def add_patient(
            self, name: str, birth_date: str,
            weight: int, height: int, sex: str
    ) -> Patient:
        """Добавляет пациента, возвращает объект пациента."""
        table = "patients"
        patient = Patient(name=name, birth_date=birth_date, weight=weight, height=height, sex=sex, uuid=str(uuid4()))
        self.storage.add_data(table=table, data=asdict(patient))
        return patient

    def add_doctor(
            self, name: str,
            category: str,
            position: str
    ) -> Doctor:
        """Добавляет доктора, возвращает объект доктора."""
        table = "doctors"
        doctor = Doctor(name=name, category=category, position=position, uuid=str(uuid4()))
        self.storage.add_data(table=table, data=asdict(doctor))
        return doctor

    def add_diagnosis(
            self, patient_uuid: str,
            doctor_uuid: str,
            description: str,
            treatment: str
    ) -> Diagnosis:
        """Добавляет новый диагноз для пациента. Возвращает объект диагноза."""
        patient = self.get_patient(patient_uuid)
        doctor = self.get_doctor(doctor_uuid)
        return Diagnosis(patient=patient, doctor=doctor, description=description, treatment=treatment)

    def get_doctor(self, doctor_uuid: str) -> Doctor:
        table = "doctors"
        where_params = {'uuid': doctor_uuid}
        data = self.storage.get_data(table=table, where=where_params)
        return Doctor(**data[0])

    def get_patient(self, patient_uuid: str) -> Patient:
        table = "patients"
        where_params = {'uuid': patient_uuid}
        data = self.storage.get_data(table=table, where=where_params)
        return Patient(**data[0])

    def get_all_doctors(self) -> List[Doctor]:
        """Вернуть список всех докторов."""
        table = "doctors"
        data = self.storage.get_data(table=table)
        return [Doctor(**doctor) for doctor in data]

    def get_all_patients(self) -> List[Patient]:
        """Вернуть список всех пациентов."""
        table = "patients"
        data = self.storage.get_data(table=table)
        return [Patient(**patient) for patient in data]

    def get_all_anamnesis(self) -> List[Diagnosis]:
        """Вернуть список всех диагнозов."""
        table = "anamnesis"
        columns = ("diagnosis",)
        data = self.storage.get_data(table=table, columns=columns)
        return [diagnosis.get('diagnosis') for diagnosis in data]

    def get_doctor_patients_count(self, doctor_uuid: str) -> int:
        """Получить количество пациентов для определенного доктора."""

    def get_bmi(self, patient_uuid: str) -> float:
        """Получить имт для определенного пациента."""
        patient = self.get_patient(patient_uuid)
        return patient.weight / (patient.height ** 2)

    def select_patients(
            self,
            name: str = None,
            sex: str = None,
            patient_uuid: str = None
    ) -> List[Patient]:
        """Выбрать пациентов по заданным критериям."""
        table = "patients"
        where_params = {"name": name,
                        "sex": sex,
                        "patient_uuid": patient_uuid}
        data = self.storage.get_data(table=table, where=where_params)
        return [Patient(**patient) for patient in data]
