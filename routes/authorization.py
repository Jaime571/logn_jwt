from flask import Blueprint, request
from flask.json import jsonify
from function_jwt import write_token, verify_token

routes_autorization = Blueprint("routes_autorization", __name__)


@routes_autorization.post("/login")
def login():
    data = request.get_json()
    print(data)
    if data['username'] == "Estela Barajas" and data['password'] == "admin":
        print ("Login successful")
        return write_token(data=request.get_json())
    else:
        response = jsonify({"message": "User not found"})
        """ response.status_code = 404 """
        return response, 404


@routes_autorization.get("/verify/token")
def verify():
    """ Falla al tener un token vacío, falta de revisar """
    token = request.headers['Authorization'].split(' ')[0]
    print(token)
    if(token):
        return verify_token(token, output=True)
    return jsonify({"message": "Empty token"}), 401
