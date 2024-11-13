from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

# Crear la app de Flask
app = Flask(__name__)

# Configuración para la base de datos y Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacto.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuración para el servidor SMTP de Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cell.shop5@gmail.com'  # Correo
app.config['MAIL_PASSWORD'] = 'mjou dvrc ctuw fcld'  # Contraseña
# Remitente del correo
app.config['MAIL_DEFAULT_SENDER'] = ("CellShop", "cell.shop5@gmail.com")

# Agregar la clave secreta necesaria para las sesiones y mensajes flash
app.secret_key = 'CellShop2024'  # Cambia esto a una clave más segura

# Inicializar las extensiones
db = SQLAlchemy(app)
mail = Mail(app)

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

# Definir el modelo de la base de datos para los contactos
class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    motivo = db.Column(db.String(50), nullable=True)
    mensaje = db.Column(db.Text, nullable=True)

# Crear la base de datos (ejecuta este bloque solo una vez)
with app.app_context():
    db.create_all()
    
# Rutas y vistas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carrito')
def carrito():
    # Aquí debes definir los productos del carrito y el estado del carrito
    # Por ejemplo, si los productos están almacenados en una lista o base de datos
    productos = []  # Simulando que el carrito está vacío
    carrito_vacio = len(productos) == 0  # Verifica si el carrito está vacío
    total = sum(producto['precio'] for producto in productos)  # Total calculado (si tienes precios)
    carrito_comprado = False  # Estado si ya se ha realizado una compra
    # Pasa las variables al template
    return render_template('carrito.html', productos=productos, carrito_vacio=carrito_vacio, total=total, carrito_comprado=carrito_comprado)

@app.route('/')
def index() -> str:
    # Consultar todos los contactos y pasarlos al template 'index.html'
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    print(f"Nombre: {name}, Email: {email}")
    
    try:
        # Crear nuevo contacto y agregarlo a la base de datos
        new_contact = Contacto(name=name, email=email)
        db.session.add(new_contact)
        db.session.commit()
        print("Contacto agregado exitosamente.")  # Los print son para depuración
    except Exception as e:
        db.session.rollback()
        print(f"Error al guardar el contacto: {e}")
    
    return redirect(url_for('index'))  # Redirigir a la vista principal

# Ruta para crear la base de datos
@app.route('/database')
def database():
    # Función para crear la base de datos
    db.drop_all()
    db.create_all()
    return "Base de datos creada correctamente."

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        motivo = request.form.get('motivo')
        mensaje = request.form.get('mensaje')

        # Validar que los campos requeridos no estén vacíos
        if not nombre or not email or not mensaje:
            flash("Por favor, completa todos los campos requeridos.", "error")
            return redirect(url_for('contactos'))

        # Aquí podrías agregar más validaciones, como verificar el formato del correo, etc.
        if '@' not in email:
            flash("El correo electrónico no es válido.", "error")
            return redirect(url_for('contactos'))

        # Lógica para procesar los datos del formulario (por ejemplo, guardar en base de datos o enviar un correo)
        # En este ejemplo, solo flash un mensaje de éxito.
        flash("¡Mensaje enviado con éxito! Nos pondremos en contacto contigo pronto.", "success")
        return redirect(url_for('contacto'))  # Redirige al formulario de contacto

    # Si es un GET, simplemente renderiza el formulario
    return render_template('contactos.html')

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
