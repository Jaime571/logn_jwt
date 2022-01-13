from flask import json
import requests
from flask_restful import Api, Resource, reqparse
from flask import Blueprint, request
from flask.json import jsonify
from function_jwt import write_token, verify_token
from verificarDatos import isValid

signUp = Blueprint("signUp", __name__)
api = Api(signUp)

item_post_args = reqparse.RequestParser()
item_post_args.add_argument(
    'username', type=str, help="nombre de usuario", required=True)
item_post_args.add_argument(
    'password', type=str, help="contrasena", required=True)
item_post_args.add_argument(
    'email', type=str, help="correo electronico", required=True)
item_post_args.add_argument(
    'nombre', type=str, help="nombre del usuario", required=True)
item_post_args.add_argument(
    'aPaterno', type=str, help="apellido paterno del usuario", required=True)
item_post_args.add_argument(
    'aMaterno', type=str, help="apellido materno del usuario", required=True)
item_post_args.add_argument(
    'fNacimiento', type=str, help="fecha de naciemiento del usuario", required=True)
item_post_args.add_argument(
    'sexo', type=str, help="sexo del usuario", required=True)
item_post_args.add_argument(
    'telefono', type=str, help="telefono del usuario", required=True)
item_post_args.add_argument(
    'codigo', type=str, help="codigo del usuario", required=True)




class Paciente(Resource):
    def post(self):
        args = item_post_args.parse_args()
        items = {
            "username": args["username"],
            "password": args["password"],
            "email": args["email"],
            "nombre": args["nombre"],
            "aPaterno": args["aPaterno"],
            "aMaterno": args["aMaterno"],
            "fNacimiento": args["fNacimiento"],
            "sexo": args["sexo"],
            "telefono": args["telefono"],
            "codigo": args["codigo"]
        }

        #Se manda validar la informacion del registro
        checkItems = isValid(items)
        
        print(checkItems.data)
        if(checkItems.status_code == 200):
            data = {"tipousuario":"Paciente", "username": args["username"], "password": args["password"]}
            #Se manda a llamar al endpoint del server. En caso de que el registro sea exitoso
            #Se manda a llamar al endpoint de creación de token
            #print(json.dumps(items, indent=3))
            #return checkItems
            
            return write_token(data)
        return checkItems

class Especialista(Resource):
    def post(self):
        args = item_post_args.parse_args()
        items = {
            "username": args["username"],
            "password": args["password"],
            "email": args["email"],
            "nombre": args["nombre"],
            "aPaterno": args["aPaterno"],
            "aMaterno": args["aMaterno"],
            "fNacimiento": args["fNacimiento"],
            "sexo": args["sexo"],
            "telefono": args["telefono"],
            "codigo": args["codigo"]
        }

        #Se manda validar la informacion del registro
        checkItems = isValid(items)
        
        print(checkItems.data)
        if(checkItems.status_code == 200):
            data = {"tipousuario":"Especialista", "username": args["username"], "password": args["password"]}
            #Se manda a llamar al endpoint del server. En caso de que el registro sea exitoso
            #Se manda a llamar al endpoint de creación de token
            #print(json.dumps(items, indent=3))
            #return checkItems
            
            return write_token(data)
        return checkItems

class Auxiliar(Resource):
    def post(self):
        args = item_post_args.parse_args()
        items = {
            "username": args["username"],
            "password": args["password"],
            "email": args["email"],
            "nombre": args["nombre"],
            "aPaterno": args["aPaterno"],
            "aMaterno": args["aMaterno"],
            "fNacimiento": args["fNacimiento"],
            "sexo": args["sexo"],
            "telefono": args["telefono"],
            "codigo": args["codigo"]
        }

        #Se manda validar la informacion del registro
        checkItems = isValid(items)
        
        print(checkItems.data)
        if(checkItems.status_code == 200):
            data = {"tipousuario":"Auxiliar", "username": args["username"], "password": args["password"]}
            #Se manda a llamar al endpoint del server. En caso de que el registro sea exitoso
            #Se manda a llamar al endpoint de creación de token
            #print(json.dumps(items, indent=3))
            #return checkItems
            
            return write_token(data)
        return checkItems


api.add_resource(Paciente, '/paciente')
api.add_resource(Especialista, '/especialista')
api.add_resource(Auxiliar, '/auxiliar')
