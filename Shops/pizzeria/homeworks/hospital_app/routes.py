from functools import wraps
from flask import jsonify, request, abort
from config import app, hospital
from storage_handler import DBException
from hospital import NotFoundException


def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DBException:
            abort(404)
        except NotFoundException:
            abort(404)

    return wrapper


@app.route("/doctors")
@error_handler
def get_doctors():
    return jsonify(hospital.get_all_doctors())


@app.route("/doctors/<string:doctor_uuid>/patients/count")
@error_handler
def patients_count(doctor_uuid):
    return jsonify({"patients_number": hospital.get_doctor_patients_count(doctor_uuid)})


@app.route("/patients", methods=["GET"])
@error_handler
def get_patients():
    return jsonify(hospital.select_patients(**request.args))


@app.route("/patients/bmi/<string:patient_uuid>")
@error_handler
def get_patient_bmi(patient_uuid):
    return jsonify({"bmi": hospital.get_bmi(patient_uuid)})
