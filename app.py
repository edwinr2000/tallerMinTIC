from flask import Flask, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

# Se listan los dominios comunes, para generar correos aleatorios con cada dominio
dominios_correo = ['@outlook.com','@gmail.com', '@hotmail.com', '@live.com','@yahoo.com','@icloud.com','@vivaldi.net','@misena.edu.co','@unal.edu.co']

# Se crea la función para generar Cadena aleatoria, que será el nombre del usuario y el correo.
def generar_cadena_aleatoria(longitud):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))

# Lista para almacenar los datos
datos = []

# Se generan los 500.000 registros al azar
for _ in range(500000):
    nombre = generar_cadena_aleatoria(5)
    correo = generar_cadena_aleatoria(5) + random.choice(dominios_correo)
    longitud_contraseña = random.randint(5, 15)  # Se genera una longitud aleatoria entre 5 y 15
    contraseña = generar_cadena_aleatoria(longitud_contraseña)  # Se usa la longitud aleatoria
    datos.append({'name': nombre, 'email': correo, 'password': contraseña})

# Se publican los datos en la API
@app.route('/ejercicioI', methods=['GET'])
def obtener_datos():
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
