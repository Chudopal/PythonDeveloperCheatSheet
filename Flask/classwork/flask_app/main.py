import flask
from flask import render_template
from flask import jsonify
from flask import request


app = flask.Flask(__name__)


class UserStorage():
    
    def __init__(self, path):
        self.path = path
        self.data = self.read()

    def find_users(self, job=None, name=None) -> list:
        response = self.data.values()

        if job:
            response = filter(
                lambda user: user.get("job").lower() == job.lower(),
                response
            )
        if name:
            response = filter(
                lambda user: user.get("name").lower() == name.lower(),
                response
            )
        
        return response

    def get_user_by_id(self, user_id):
        return self.data.get(str(user_id))

    def save(self):
        import json
        with open(self.path, "w") as file:
            json.dump(file, self.data)
    
    def read(self):
        import json
        with open(self.path) as file:
            result = json.load(file)
        return result


@app.route("/users/", methods=["GET"])
def get_users():
    name = request.args.get("name")
    job = request.args.get("job")
    response = UserStorage('1.json').find_users(name=name, job=job)
    return jsonify(list(response))


@app.route("/users/html/<int:user_id>", methods=["GET"])
def create_user(user_id):
    user = UserStorage('1.json').get_user_by_id(user_id=user_id)
    return render_template(
        "users.html",
        name=user.get("name"),
        job=user.get("job")
    )



@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    name = request.args.get("name")
    job = request.args.get("job")

    return jsonify({"name": name, "job": job})



app.run(port=5555)


'''
http://127.0.0.1:5555/users/?name=alex&job=dev
'''