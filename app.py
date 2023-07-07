# Importamos el metodo random para generar auto-legajo 
import random
#Importamos las clases para enviar el email
import smtplib
from email.message import EmailMessage

from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, url_for)

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)