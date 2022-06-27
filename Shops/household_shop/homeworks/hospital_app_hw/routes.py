from flask import Flask, jsonify
from hospital import Hospital


app = Flask(__name__)
hospital = Hospital()


@app.route("/doctors/<doctor_uuid>/patients/count")
def get_patients_by_docid(doctor_uuid: str):
    return jsonify({"cnt_patients": hospital.get_doctor_patients_count(doctor_uuid)})


@app.route("/patients/bmi/<patient_uuid>")
def get_bmi(patient_uuid):
    return jsonify({"bmi": hospital.get_bmi(patient_uuid)})


@app.route("/doctors")
def get_all_doctors():
    return jsonify({"bmi": hospital.get_all_doctors()})   


@app.route("/patients")
def select_patients():
    hospital.select_patients()


@app.route("/doctors")
def get_all_doctors():
    hospital.get_all_doctors()


app.run(port=5000)
