from flask import Flask
app = Flask(__name__)
app.secret_key = 'secreto'

BASE_DATOS = 'dojos_y_ninjas'