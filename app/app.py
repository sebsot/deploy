from flask import Flask, jsonify, render_template
from logging import FileHandler, WARNING
import sys
import os
import mysql.connector

app = Flask(__name__, template_folder = 'templates')



def datos_participantes():
    secret_path_user = "$HOME/credenciales/user.txt"
    secret_path_pass = "$HOME/credenciales/password.txt"

    with open(secret_path_user, "r") as secret_file:
        user = secret_file.read().strip()
    

    with open(secret_path_pass, "r") as secret_file:
        pwd = secret_file.read().strip()
    
    config = {
        'user': user,
        'password': pwd,
        'host': 'db',
        'port': '3306',
        'database': 'dbproyecto'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT NOMBRE_ALUMNO, CARRERA FROM participantes')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/index')
@app.route('/')
def index():
    participantes = datos_participantes()
    return render_template('index.html', participantes=participantes)

@app.route('/participantes')
def estudiantes():
    return jsonify({'estudiantes': datos_participantes()})

@app.route('/probando')
def hola():
    return 'hola!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
