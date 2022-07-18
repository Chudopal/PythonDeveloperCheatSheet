from flask import Flask
from hospital import Hospital
from storage_handler import DBStorage
from query_builder import Table

DB_CONNECTION_CONFIG = {
    'host': "localhost",
    'user': "admin",
    'password': "admin",
    'dbname': "homeworks"
}

storage = DBStorage(**DB_CONNECTION_CONFIG)

doctors = Table('doctors', 'uuid', 'name', 'category', 'position')
anamnesis = Table('anamnesis', 'anamnesis', 'patient_uuid', 'doctor_uuid', 'diagnosis', 'treatment')
patients = Table('patients', 'uuid', 'name', 'birth_date', 'weight', 'height', 'sex')

hospital = Hospital(storage=storage, patients=patients, doctors=doctors, anamnesis=anamnesis)

app = Flask(__name__)
