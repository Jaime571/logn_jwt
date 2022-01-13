import re

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

