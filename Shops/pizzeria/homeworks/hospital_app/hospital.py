from typing import List
from uuid import uuid4
from dataclasses import asdict
from models import Doctor, Patient, Diagnosis
from query_builder import Table, count


class NotFoundException(Exception):
    def __str__(self):
        return "Object not found"


class Hospital:

    def __init__(self, storage: 'DB Storage', patients: 'Table', doctors: 'Table', anamnesis: 'Table'):
        self.storage = storage
        self.patients = patients
        self.doctors = doctors
        self.anamnesis = anamnesis

    def add_patient(
            self, name: str, birth_date: str,
            weight: int, height: int, sex: str
    ) -> Patient:
        """Добавляет пациента, возвращает объект пациента."""
        patient = Patient(name=name, birth_date=birth_date, weight=weight, height=height, sex=sex, uuid=str(uuid4()))
        query = self.patients.insert(asdict(patient)).query
        self.storage.execute(query)
        return patient

    def add_doctor(
            self, name: str,
            category: str,
            position: str
    ) -> Doctor:
        """Добавляет доктора, возвращает объект доктора."""
        doctor = Doctor(name=name, category=category, position=position, uuid=str(uuid4()))
        query = self.doctors.insert(asdict(doctor)).query
        self.storage.execute(query)
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
        diagnosis = Diagnosis(patient=patient, doctor=doctor, description=description, treatment=treatment)
        query = self.anamnesis.insert(asdict(diagnosis)).query
        self.storage.execute(query)
        return diagnosis

    def get_doctor(self, doctor_uuid: str) -> Doctor:
        where_params = {'uuid': doctor_uuid}
        query = self.doctors.select().where(where_params).query
        data = self.storage.execute(query)
        if data:
            return Doctor(**data[0])
        else:
            raise NotFoundException

    def get_patient(self, patient_uuid: str) -> Patient:
        where_params = {'uuid': patient_uuid}
        query = self.patients.select().where(where_params).query
        data = self.storage.execute(query)
        if data:
            return Patient(**data[0])
        else:
            raise NotFoundException

    def get_all_doctors(self) -> List[Doctor]:
        """Вернуть список всех докторов."""
        query = self.doctors.select().query
        data = self.storage.execute(query)
        return [Doctor(**doctor) for doctor in data]

    def get_all_patients(self) -> List[Patient]:
        """Вернуть список всех пациентов."""
        query = self.patients.select().query
        data = self.storage.execute(query)
        return [Patient(**patient) for patient in data]

    def get_all_anamnesis(self) -> List[Diagnosis]:
        """Вернуть список всех диагнозов."""
        join_params = {
            self.patients: (self.patients.uuid, self.anamnesis.patient_uuid),
            self.doctors: (self.doctors.uuid, self.anamnesis.doctor_uuid)
        }
        query = self.anamnesis.select(
            self.patients.uuid.as_('patient_uuid'),
            self.patients.name.as_('patient_name'),
            self.patients.birth_date.as_('patient_birth_date'),
            self.patients.weight.as_('patient_weight'),
            self.patients.height.as_('patient_height'),
            self.patients.sex.as_('patient_sex'),
            self.doctors.uuid.as_('doctor_uuid'),
            self.doctors.name.as_('doctor_name'),
            self.doctors.category.as_('doctor_category'),
            self.doctors.position.as_('doctor_position'),
            self.anamnesis.diagnosis.as_('diagnosis'),
            self.anamnesis.treatment.as_('treatment')
        ).join_on(join_params).query
        data = self.storage.execute(query)
        return [
            Diagnosis(
                doctor=Doctor(
                    name=diagnosis.get('doctor_name'),
                    position=diagnosis.get('doctor_position'),
                    category=diagnosis.get('doctor_category'),
                    uuid=diagnosis.get('doctor_uuid')
                ),
                patient=Patient(
                    name=diagnosis.get('patient_name'),
                    birth_date=diagnosis.get('patient_birth_date'),
                    weight=diagnosis.get('patient_weight'),
                    height=diagnosis.get('patient_height'),
                    sex=diagnosis.get('patient_sex'),
                    uuid=diagnosis.get('patient_uuid')
                ),
                description=diagnosis.get('diagnosis'),
                treatment=diagnosis.get('treatment')
            )
            for diagnosis in data
        ]

    def get_doctor_patients_count(self, doctor_uuid: str) -> int:
        """Получить количество пациентов для определенного доктора."""
        join_params = {
            self.anamnesis: (self.doctors.uuid, self.anamnesis.doctor_uuid)
        }
        where_params = {'anamnesis.doctor_uuid': doctor_uuid}
        query = self.doctors.select(count(self.anamnesis.patient_uuid)).join_on(join_params).where(where_params).query
        data = self.storage.execute(query)
        return data[0].get('count')

    def get_bmi(self, patient_uuid: str) -> float:
        """Получить имт для определенного пациента."""
        patient = self.get_patient(patient_uuid)
        return round(patient.weight / (patient.height ** 2), 2)

    def select_patients(
            self,
            name: str = None,
            sex: str = None,
            patient_uuid: str = None
    ) -> List[Patient]:
        """Выбрать пациентов по заданным критериям."""
        where_params = {}
        if name:
            where_params.update({"name": name})
        if sex:
            where_params.update({"sex": sex})
        if patient_uuid:
            where_params.update({"uuid": patient_uuid})
        query = self.patients.select().where(where_params).query
        data = self.storage.execute(query)
        if data:
            return [Patient(**patient) for patient in data]
        else:
            raise NotFoundException
