from flask import Blueprint, jsonify, request

# 1. Crear el Blueprint
socios_bp = Blueprint('socios', __name__, url_prefix='/socios')