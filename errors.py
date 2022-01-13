from flask import make_response, jsonify

usernameError = make_response(
    jsonify({"message": "El nombre de usuario no es valido."}), 400)
passwordError = make_response(
    jsonify({"message": "La contrasna no es valida."}), 400)
emailError = make_response(
    jsonify({"message": "El correo electronico no es valido."}), 400)
NombreError = make_response(
    jsonify({"message": "El nombre no es valida."}), 400)
aPaternoError = make_response(
    jsonify({"message": "El apellido paterno no es valida."}), 400)
aMaternoError = make_response(
    jsonify({"message": "El apellido materno no es valida."}), 400)
fNacimientoError = make_response(
    jsonify({"message": "La fecha de nacimiento no es valida."}), 400)
sexoError = make_response(
    jsonify({"message": "El sexo no es valida."}), 400)
telefonoError = make_response(
    jsonify({"message": "El telefono no es valida."}), 400)
codigoError = make_response(
    jsonify({"message": "El codigo no es valida."}), 400)
