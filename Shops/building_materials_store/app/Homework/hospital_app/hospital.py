from typing import List
from models import Doctor, Patient, Diagnosis
import psycopg2


class DB_Handler:
    def __init__(self):
        self.dbname = 'Clinic_SQL'
        self.user = 'postgres'
        self.connection = psycopg2.connect(dbname=self.dbname, user=self.user)
        self.cursor = self.connection.cursor()

    def DB_reader(self, columns, table_name):
        self.cursor.execute(
            """SELECT {columns} FROM {table};""".format(columns=columns, table=table_name)
        )
        DB_list = self.cursor.fetchall()
        return DB_list

    def format_product_DB(self, product) -> str:
        return '\n'.join([
            f'{product_name} - {cost} руб'
            for id, product_name, cost in product
        ])


class Hospital:

    def add_patient(
            self, name: str, birth_date: str,
            weight: int, height: int, sex: str
    ) -> Patient:
        """Добавляет пациента, возвращает объект пациента."""

        self.cursor.execute(
            """INSERT INTO patients (name, birth_date, weight, height, sex)
            VALUES
            ('{name}', '{birth_date}', '{weight}', '{height}', '{sex}')"""
            .format(name=name, birth_date=birth_date, weight=weight, height=height, sex=sex)
        )
        self.connection.commit()

    def add_doctor(
            self, name: str,
            category: str,
            position: str
    ) -> Doctor:
        """Добавляет доктора, возвращает объект доктора."""

        self.cursor.execute(
            """INSERT INTO doctors(name, category, position)
            VALUES
            ('{name}', '{category}', '{position}')"""
            .format(name=name, category=category, position=position)
        )
        self.connection.commit()

    def add_diagnosis(
            self, patient_uuid: str,
            doctor_uuid: str,
            description: str,
            treatment: str,
            name: str,
    ) -> Diagnosis:
        """Добавляет новый диагноз для пациента. Возвращает объект диагноза."""

        self.cursor.execute(
            """INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
            SELECT '{patient_uuid}', '{doctor_uuid}', '{description}', '{treatment}
            FROM patients WHERE name='{name}'"""
            .format(patient_uuid=patient_uuid, doctor_uuid=doctor_uuid, description=description, treatment=treatment,
                    name=name)
        )
        self.connection.commit()

    def get_all_doctors(self, columns, table_name) -> List[Doctor]:
        """Вернуть список всех докторов."""
        doctors = DB_Handler().DB_reader(columns, table_name)
        return doctors

    def get_all_patients(self, columns, table_name) -> List[Patient]:
        """Вернуть список всех пациентов."""
        patients = DB_Handler().DB_reader(columns, table_name)
        return patients

    def get_all_anamnesis(self, columns, table_name) -> List[Diagnosis]:
        """Вернуть список всех диагнозов."""
        anamnesis = DB_Handler().DB_reader(columns, table_name)
        return anamnesis

    # def get_doctor_patients_count(self, doctor_uuid: str) -> int:
    #     """Получить количество пациентов для определенного доктора."""
    #
    #     self.cursor.execute(
    #         """SELECT count(DISTINCT anamnesis.patient_uuid), doctors.name
    #         FROM doctors
    #         JOIN anamnesis ON anamnesis.doctor_uuid=doctors.uuid
    #         GROUP BY doctors.name;"""
    #         .format(...)
    #     )
    #     self.connection.commit()

    def get_bmi(self, patient_uuid: str) -> float:
        """Получить имт для определенного пациента."""

    def select_patients(
            self, name: str = None,
            sex: str = None, patient_uuid: str = None
    ) -> List[Patient]:
        """Выбрать пациентов по заданным критериям."""


print(Hospital().get_all_doctors(columns='name', table_name='doctors'))
print(Hospital().get_all_patients(columns='name', table_name='patients'))
print(Hospital().get_all_anamnesis(columns='diagnosis', table_name='anamnesis'))
