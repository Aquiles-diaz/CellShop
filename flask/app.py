
from typing import List, Tuple, Any
from flask import render_template, request, Response, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user, LoginManager
from flask_mail import Mail, Message
from sqlalchemy import func
import random
import string
from src.models import *
from src.routes import main

app = crear_app()
app.register_blueprint(main)

# Inicializa Flask-Login
login_manager = LoginManager()
login_manager.login_message = None
login_manager.init_app(app)

# Redireccionar a la página de login si no está autenticado
login_manager.login_view = "login"  # Vista de login

# Función para cargar el usuario a partir de su ID
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


# Configuración para el servidor SMTP de Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mateando.ando6@gmail.com'  # Correo
app.config['MAIL_PASSWORD'] = 'mjou dvrc ctuw fcld'  # Contraseña
# Remitente del correo
app.config['MAIL_DEFAULT_SENDER'] = ("Mateando", "mateando.ando6@gmail.com")

mail = Mail(app)

@app.route('/database')
def database():
    init_db()
    return "Base de datos creada correctamente."

def create_db():
    db.drop_all()
    db.create_all()
