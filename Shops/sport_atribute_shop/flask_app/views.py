from config import app
from flask import request, jsonify, make_response
from service import registrate, login as log

@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    token = log(data)
    return make_response(jsonify({"token": token}), 200)


@app.route('/reg', methods=["POST"])
def reg():
    data = request.get_json()
    registrate(data)
    return make_response(jsonify({"result": 'OK'}), 201)