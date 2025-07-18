from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Instanciamos las extensiones
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Cargar configuración desde config.py
    db.init_app(app)

    # Importar y registrar blueprints
    from app.routes.actividades import bp as actividades_bp
    app.register_blueprint(actividades_bp)

    with app.app_context():
        db.create_all()

    return app