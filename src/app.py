from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager, UserMixin
import json

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacto.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cell.shop5@gmail.com'
app.config['MAIL_PASSWORD'] = 'mjou dvrc ctuw fcld'
app.config['MAIL_DEFAULT_SENDER'] = ("CellShop", "cell.shop5@gmail.com")
app.secret_key = 'CellShop2024'

# Inicialización de extensiones
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_message = None
login_manager.login_view = "login"

# Modelos de base de datos
class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(55), nullable=False)  # correcion de que 'nombre' esta aca
    email = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    motivo = db.Column(db.String(50), nullable=True)
    mensaje = db.Column(db.Text, nullable=True)

# Cargar usuario para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Creación de la base de datos
with app.app_context():
    db.create_all()

# Rutas de la aplicación
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        motivo = request.form.get('motivo')
        mensaje = request.form.get('mensaje')

        # Validaciones del formulario
        if not nombre or not email or not mensaje:
            flash("Por favor, completa todos los campos requeridos.", "error")
            return redirect(url_for('contacto'))

        if '@' not in email:
            flash("El correo electrónico no es válido.", "error")
            return redirect(url_for('contacto'))

        # Guardar en la base de datos
        try:
            nuevo_contacto = Contacto(nombre=nombre, email=email, telefono=telefono, motivo=motivo, mensaje=mensaje)
            db.session.add(nuevo_contacto)
            db.session.commit()
            flash("¡Mensaje enviado con éxito! Nos pondremos en contacto contigo pronto.", "success")
        except Exception as e:
            db.session.rollback()  # Rollback de la sesión para evitar cambios parciales
            flash("Error al enviar el mensaje. Por favor, inténtalo de nuevo.", "error")
            print(f"Error al guardar el contacto: {e}")  # Mensaje en consola para depuración
            import traceback
            traceback.print_exc()  # Imprime más detalles sobre el error
        return redirect(url_for('contacto'))

    return render_template('contactos.html')

@app.route('/carrito')
def carrito():
    try:
        with open('productos.json', 'r') as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        print("El archivo 'celulares.json' no se encuentra.")
        productos = []

    carrito_vacio = len(productos) == 0
    total = sum(producto['precio'] for producto in productos if 'precio' in producto)

    # Imprimir los productos y el total para verificar
    print("Productos:", productos)
    print("Total:", total)

    return render_template('carrito.html', productos=productos, carrito_vacio=carrito_vacio, total=total)


# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
