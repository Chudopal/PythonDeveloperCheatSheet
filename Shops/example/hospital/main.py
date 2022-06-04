from typing import List
import psycopg2


class Persone:
    
    def __init__(self, name: str = None, uuid: str=None):
        self.name = name
        self.uuid = uuid


class Patient(Persone):
    
    def __init__(
        self, name: str, uuid: str,
        height: int, weight: int, birth_date, sex: str
    ):
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.sex = sex
        super().__init__(name=name, uuid=uuid)

    def __repr__(self):
        return f"name - {self.name}\nI'm patient\n"


class Doctor(Persone):
    
    def __init__(self, name, uuid=None, category=None, position=None):
        self.category = category
        self.position = position
        super().__init__(name=name, uuid=uuid)
    
    def __repr__(self):
        return f"name - {self.name}\nI'm doctor\n"


class Diagnosis:

    def __init__(
        self, description: str,
        treatment: str, doctor: Doctor,
        patient: Patient
    ):
        self.description = description
        self.treatment = treatment
        self.doctor = doctor
        self.patient = patient
    
    def __repr__(self):
        return f"description - {self.description}"\
            f"\ndoctor - {self.doctor.name}"\
            f"\npatient - {self.patient.name}\n"


class HospitalRepository:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_all_patients(self):
        self.cursor.execute("SELECT * FROM patients;")
        patients = self.cursor.fetchall()
        return self._create_patients(patients)

    def get_all_doctors_patients(self, doctor: Doctor):
        self.cursor.execute("""
            SELECT patients.uuid, patients.name, height, weight,
            birth_date, sex
            FROM doctors
            JOIN anamnesis ON doctor_uuid=doctors.uuid
            JOIN patients ON patients.uuid=patient_uuid 
            WHERE doctors.uuid = '{}';
        """.format(doctor.uuid))
        patients = self.cursor.fetchall()
        return self._create_patients(patients)
        

    def get_patient_anamnesis(self, patient: Patient):
        pass

    def get_doctor_by_name(self, name: str) -> Doctor:
        self.cursor.execute(
        """SELECT * FROM doctors WHERE name = '{}';
        """.format(name)
        )
        raw_doctor = self.cursor.fetchone()
        return self._create_doctor(raw_doctor)


    def _create_doctor(self, raw_doctor):
        return Doctor(
            uuid=raw_doctor[0],
            name=raw_doctor[1],
            category=raw_doctor[2],
            position=raw_doctor[3]
        )


    def _create_patients(self, patients: List[Patient]):
        return [
            Patient(
                uuid=patient[0],
                name=patient[1],
                birth_date=patient[2],
                weight=patient[3],
                height=patient[4],
                sex=patient[5]
            ) for patient in patients
        ]


class Hospital():
    
    def __init__(self, hr):
        self.hr = hr

    def get_doctor_by_name(self):
        name = input("Enter doctor's name: ")
        doctor = self.hr.get_doctor_by_name(name)
        patients = self.hr.get_all_doctors_patients(doctor)
        for p in patients:
            print(p)


connection = psycopg2.connect(
    dbname='clinic_lesson',
    user='admin',
    password='admin',
    host='localhost',
    port=5432
)

hr = HospitalRepository(connection=connection)

hos = Hospital(hr)

hos.get_doctor_by_name()