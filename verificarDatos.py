from flask import jsonify, make_response
import re, time


def isValid(data: dict):

    # Se obtienen los valores del diccionario entrante
    username = data['username']
    password = data['password']
    email = data['email']
    nombre = data['nombre']
    aPaterno = data['aPaterno']
    aMaterno = data['aMaterno']
    fNacimiento = data['fNacimiento']
    sexo = data['sexo']
    telefono = data['telefono']
    codigo = data['codigo']

    # Se defineen los patrones de las expresiones regulares para validar los campos
    usernamePattern = r'\A[A-Z]'  # Debe contener una mayúscula
    # Debe tener una mayúscula, 1 número, 1 caracter especial y ser de mínimo 8 dígitos máx 16
    passwordPattern = r'^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$'
    # Debe tener al menos 5 caracteres antes del @ y contar con dominio gmail o googlemail y terminar en .com
    emailPattern = r'^\w(\.?\w){5,}@g(oogle)?mail\.com$'
    nombrePattern = r'^\A[A-Z]'  # Debe tener mayúsculas
    aPaternoPattern = r'^\A[A-Z]'  # Debe tener mayúsculas
    aMaternoPattern = r'^\A[A-Z]'  # Debe tener mayúsculas
    # Valida que la fecha de nacimiento esté dada en formato DD/MM/AAAA y no sea menor a 1900 o mayor a 2090
    fNacimientoPattern = r'(?:0[1-9]|[12][0-9]|3[01])[-/.](?:0[1-9]|1[012])[-/.](?:19\d{2}|20[01][0-9]|2020)\b'
    sexoPattern = r'(M|F)'  # Verifica que se encuentre o M o F
    # Verifica que el número de teléfono sea de 10 dígitos
    telefonoPattern = r'\d{10}'
    codigoPattern = r'^\w{8}'  # Verifica que el código contenga 8 dígitos

    # Se hace la verificación
    usernameIsValid = re.search(usernamePattern, username)
    passwordIsValid = re.search(passwordPattern, password)
    emailIsValid = re.search(emailPattern, email)
    nombreIsValid = re.search(nombrePattern, nombre)
    aPaternoIsValid = re.search(aPaternoPattern, aPaterno)
    aMaternoIsValid = re.search(aMaternoPattern, aMaterno)
    fNacimientoIsValid = re.search(fNacimientoPattern, fNacimiento)
    sexoIsValid = re.search(sexoPattern, sexo)
    telefonoIsValid = re.search(telefonoPattern, telefono)
    codigoIsValid = re.search(codigoPattern, codigo)

    verifyed = [usernameIsValid, passwordIsValid, emailIsValid, nombreIsValid, aPaternoIsValid,
              aMaternoIsValid, fNacimientoIsValid, sexoIsValid, telefonoIsValid, codigoIsValid]

    usernameError = make_response(jsonify({"message": "El nombre de usuario no es valido."}), 400)
    passwordError = make_response(jsonify({"message": "La contrasna no es valida."}), 400)
    emailError = make_response(jsonify({"message": "El correo electronico no es valido."}), 400)
    NombreError = make_response(jsonify({"message": "El nombre no es valida."}), 400)
    aPaternoError = make_response(jsonify({"message": "El apellido paterno no es valida."}), 400)
    aMaternoError = make_response(jsonify({"message": "El apellido materno no es valida."}), 400)
    fNacimientoError = make_response(jsonify({"message": "La fecha de nacimiento no es valida."}), 400)
    sexoError = make_response(jsonify({"message": "El sexo no es valida."}), 400)
    telefonoError = make_response(jsonify({"message": "El telefono no es valida."}), 400)
    codigoError = make_response(jsonify({"message": "El codigo no es valida."}), 400)

    errorStatus = [usernameError, passwordError, emailError, NombreError, aPaternoError, aMaternoError,
                  fNacimientoError, sexoError, telefonoError, codigoError]

    for valueStatus, errorStatus in zip(verifyed, errorStatus):
        if(valueStatus is None):
            print(valueStatus, errorStatus)
            return errorStatus
        print(valueStatus)

    return jsonify({"user": data})

def validateOccupation(nombre, aPaterno, aMaterno, codigo):
    
    return 