from flask import Flask, jsonify
from config import hospital


app = Flask(__name__)


@app.route("/doctors/<doctor_uuid>/patients/count")
def get_patients_by_docid(doctor_uuid: str):
    return jsonify({"cnt_patients": hospital.get_doctor_patients_count(doctor_uuid)})


@app.route("/patients/bmi/<patient_uuid>")
def get_bmi(patient_uuid):
    return jsonify({"bmi": hospital.get_bmi(patient_uuid)})


@app.route("/doctors")
def get_all_doctors():
    return jsonify({"doctors": hospital.get_all_doctors()})   


@app.route("/patients")
def get_all_patients():
    return jsonify({"patients": hospital.get_all_patients()})  


@app.route("/anamnesis")
def get_all_anamnesis():
    return jsonify({"anamnesis": hospital.get_all_anamnesis()})
