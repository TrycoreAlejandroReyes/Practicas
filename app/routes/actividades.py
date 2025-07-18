from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.actividades import Actividades
from datetime import datetime

bp = Blueprint('actividades', __name__)

@bp.route('/', methods=['GET'])
def index():
    fecha_filtro = request.args.get('fechaFiltro')
    if fecha_filtro:
        try:
            fecha = datetime.strptime(fecha_filtro, '%Y-%m-%d').date()
            actividades = Actividades.query.filter(db.func.date(Actividades.fechaActividad) == fecha).all()
        except ValueError:
            actividades = Actividades.query.all()
    else:
        actividades = Actividades.query.all()
    return render_template('actividades/index.html', actividades=actividades)

@bp.route('/actividades/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre_actividad = request.form.get('nombreActividad')
        descripcion_actividad = request.form.get('descripcionActividad')
        fecha_actividad_str = request.form.get('fechaActividad')
        fecha_actividad = datetime.strptime(fecha_actividad_str, '%Y-%m-%d') if fecha_actividad_str else None
        nueva_actividad = Actividades(
            nombreActividad=nombre_actividad,
            descripcionActividad=descripcion_actividad,
            fechaActividad=fecha_actividad
        )
        db.session.add(nueva_actividad)
        db.session.commit()
        return redirect(url_for('actividades.index'))
    return render_template('actividades/add.html')

@bp.route('/actividades/delete/<int:id>', methods=['POST'])
def delete(id):
    actividad = Actividades.query.get_or_404(id)
    db.session.delete(actividad)
    db.session.commit()
    return redirect(url_for('actividades.index'))