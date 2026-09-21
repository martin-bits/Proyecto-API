from flask import Blueprint, jsonify, request

# 1. Crear el Blueprint
canchas_bp = Blueprint('canchas', __name__, url_prefix='/canchas')