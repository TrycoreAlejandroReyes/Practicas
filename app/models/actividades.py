from app import db
from datetime import datetime

class Actividades(db.Model):
    __tablename__ = 'actividades'
    idActividad = db.Column(db.Integer, primary_key=True)
    nombreActividad = db.Column(db.String(255), nullable=False)
    descripcionActividad = db.Column(db.Text, nullable=False)
    fechaActividad = db.Column(db.DateTime, default=datetime.utcnow)