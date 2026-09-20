from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)

# Configuración de la Base de Datos
api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db_club:TP_club2026@localhost/db_club'

# Importante para evitar advertencias de SQLAlchemy
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(api)