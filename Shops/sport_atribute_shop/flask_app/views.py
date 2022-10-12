from config import app
from flask import request, jsonify, make_response
from service import registrate, login as log


@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    try:
        token = log(data)
        result = ({"token": token,
                  "status": "ok"}, 200)
    except Exception as e:
        result = ({
            "status": "error",
            "detail": "Passwords or email didn't match.",
        }, 400)
    return make_response(jsonify(result))


@app.route('/reg', methods=["POST"])
def reg():
    data = request.get_json()
    code = 200
    result = registrate(data)
    if result.get('error'):
        code = 422
    return make_response(jsonify({"message": result.get("message")})), code
    