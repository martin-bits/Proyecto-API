from flask import Blueprint, jsonify, request

# 1. Crear el Blueprint
reservas_bp = Blueprint('reservas', __name__, url_prefix='/reservas')