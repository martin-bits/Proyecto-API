from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la Base de Datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db_club:TP_club2026@localhost/db_club'

# Importante para evitar advertencias de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 1. Importar los blueprints
from bp_routes.socios_bp import socios_bp
from bp_routes.canchas_bp import canchas_bp
from bp_routes.reservas_bp import reservas_bp

# 2. REGISTRARLOS en la app
app.register_blueprint(socios_bp)
app.register_blueprint(canchas_bp)
app.register_blueprint(reservas_bp)