from flask import jsonify, request
from config import app
from reg_service import RegService


@app.route('/reg', methods=['POST'])
def user_registration():
    reg_service = RegService(request.get_json())
    result = reg_service.credentials_ctrl()
    if not result:
        result = reg_service.check_user_data_for_reg()
    return jsonify(result)


@app.route('/auth', methods=['POST'])
def user_authentication():
    reg_service = RegService(request.get_json())
    result = reg_service.credentials_ctrl()
    if not result:
        result = reg_service.check_user_data_for_auth()
    return jsonify(result)
