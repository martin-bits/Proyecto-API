from flask import Flask
from flask_sqlalchemy import SQLAlchemy

API = Flask(__name__)

# Configuración de la Base de Datos
API.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db_club:TP_club2026@localhost/db_club'

# Importante para evitar advertencias de SQLAlchemy
API.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(API)