import uuid
import psycopg2
from typing import List
# from config import DB_CONNECTION
from models import Doctor, Patient, Diagnosis


DB_CONNECTION = {
    "dbname": "hospital_system",
    "user": "postgres",
    "password": "Vl987654321",
    "host": "localhost",
}


connection = psycopg2.connect(
    dbname=DB_CONNECTION.get("dbname"),
    user=DB_CONNECTION.get("user"),
    password=DB_CONNECTION.get("password"),
    host=DB_CONNECTION.get("host"),
)

cursor = connection.cursor() 


class DoctorRepo:

    def add_doctor(self):
        return """
            INSERT INTO patients(name, category, position)
            VALUES ({}, {}, {}, {}}, {}),
        """


    def get_all_doctors(self):
        return "SELECT * FROM doctors;"


    def get_doctor_patients_count(self):
        return """
            SELECT name, COUNT(DISTINCT anamnesis.patient_uuid) FROM doctors
            JOIN anamnesis ON doctors.uuid = '{}'
            GROUP BY name;
        """


class PatientRepo:
    
    def add_patient(self):
        return """
            INSERT INTO patients(name, birth_date, weight, height, sex)
            VALUES ({}, {}, {}, {}}, {}),
        """


    def get_all_patients(self):
        return "SELECT * FROM patients;"


    def get_bmi(self):
        return """
        SELECT (weight / (height * height * 0.0001)) as patient_bmi FROM patients
		WHERE uuid = '{}';
        """


    def select_patients(self):
        pass


class DiagnosisRepo:
    
    def add_diagnosis(self):
        return """
            INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
            VALUES (
                (SELECT uuid FROM patients WHERE name='Bob'),
                (SELECT uuid FROM doctors WHERE name='Sam'),
                'broken leg',
                'set a plaster cast'
            )
        """

    def get_all_anamnesis(self):
        return "SELECT * FROM anamnesis;"


class Hospital:

    def __init__(self) -> None:
        self.patients_repo = PatientRepo()
        self.doctor_repo = DoctorRepo()
        self.diagnosis_repo = DiagnosisRepo()


    def _get_select_data(self):
        connection.commit()
        return cursor.fetchall()


    def add_patient(
        self, name: str, birth_date: str,
        weight: int, height: int, sex: str
    ) -> Patient:
        """Добавляет пациента, возвращает объект пациента."""


    def add_doctor(
        self, name: str,
        category: str,
        position: str
    ) -> Doctor:
        """Добавляет доктора, возвращает объект доктора."""


    def add_diagnosis(
        self, patient_uuid: str,
        doctor_uuid: str,
        description: str,
        treatment: str
    ) -> Diagnosis:
        """Добавляет новый диагноз для пациента. Возвращает объект диагноза."""


    def get_all_doctors(self) -> List[Doctor]:
        """Вернуть список всех докторов."""
        cursor.execute(
            self.doctor_repo.get_all_doctors()
        )

        return self._get_select_data()


    def get_all_patients(self) -> List[Patient]:
        """Вернуть список всех пациентов."""
        cursor.execute(
            self.patients_repo.get_all_patients()
        )

        return self._get_select_data()


    def get_all_anamnesis(self) -> List[Diagnosis]:
        """Вернуть список всех диагнозов."""
        cursor.execute(
            self.diagnosis_repo.get_all_anamnesis()
        )

        return self._get_select_data()


    def get_doctor_patients_count(self, doctor_uuid: str) -> int:
        """Получить количество пациентов для определенного доктора."""
        cursor.execute(
            self.doctor_repo.get_doctor_patients_count().format(doctor_uuid)
        )

        return self._get_select_data()


    def get_bmi(self, patient_uuid: str) -> float:
        """Получить имт для определенного пациента."""
        cursor.execute(
            self.patients_repo.get_bmi().format(patient_uuid)
        )

        return self._get_select_data()


    def select_patients(
        self, name: str=None,
        sex: str=None, patient_uuid: str=None
    ) -> List[Patient]:
        """Выбрать пациентов по заданным критериям."""

