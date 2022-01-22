from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify

"""Función que sirve para obtener el tiempo de vida del token"""


def data_expiration(days: int):
    time = datetime.now()
    new_time = time + timedelta(days)
    return new_time


""" Función que se encarga de obtener los token mediante la variable data. Recibe un diccionario de datos. """


def write_token(data: dict):
    token = encode(payload={**data, "exp": data_expiration(2)},
                   key=getenv("SECRET"), algorithm="HS256")
    """ Se utiliza decode para poder serializarlo en JSON pues es un objeto de tipo bytes """
    response = token
    return jsonify({"token": response})


def verify_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms="HS256")
        decode(token, key=getenv("SECRET"), algorithms="HS256")
        """ Excepción que salta en caso de que el token no sea del mismo tipo que el definido """
    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid token"})
        """ response.status_code = 401 """
        return response, 401
        """ Excepción que salta en caso de que el token haya expirado """
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Expired token"})
        return response, 401

    except exceptions.InvalidTokenError:
        response = jsonify({"message": "Empty token"})
        return response, 401
