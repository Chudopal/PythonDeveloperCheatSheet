from typing import List
from models import Doctor, Patient, Diagnosis

class Hospital:
    
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

    def get_all_patients(self) -> List[Patient]:
        """Вернуть список всех пациентов."""

    def get_all_anamnesis(self) -> List[Diagnosis]:
        """Вернуть список всех диагнозов."""

    def get_doctor_patients_count(self, doctor_uuid: str) -> int:
        """Получить количество пациентов для определенного доктора."""
    
    def get_bmi(self, patient_uuid: str) -> float:
        """Получить имт для определенного пациента."""
    
    def select_patients(
        self, name: str=None,
        sex: str=None, patient_uuid: str=None
    ) -> List[Patient]:
        """Выбрать пациентов по заданным критериям."""