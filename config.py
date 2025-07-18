import os

# Obtiene la ruta absoluta del directorio donde se encuentra este archivo
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # URI de la base de datos SQLite en un archivo 'app.db' en el mismo directorio
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Desactiva la señalización de modificaciones de objetos -- mejora rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Ejemplo de otras configuraciones comunes:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alejandro'
    DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
