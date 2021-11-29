from flask import Blueprint, request
from flask.json import jsonify
from function_jwt import write_token, verify_token

routes_autorization = Blueprint("routes_autorization", __name__)

@routes_autorization.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    if data['username'] == "Estela Barajas" and data['password'] == "admin":
        return write_token(data = request.get_json())
    else:
       response = jsonify({"message" : "User not found"})
       response.status_code = 404
       return response

@routes_autorization.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(' ')[1]
    return verify_token(token, output = True)