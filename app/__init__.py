from flask import (Flask, 
                   render_template, 
                   request,
                   redirect,
                   url_for,
                   flash
                   )
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from models.ModeloLibro import ModeloLibro
from models.ModeloUsuario import ModeloUsuario
from models.entities.Usuario import Usuario
from flask_login import (LoginManager, 
                         login_user, 
                         logout_user, 
                         login_required,
                         current_user,
                         )

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
bootstrap = Bootstrap5(app)
login_manager_app = LoginManager(app)

@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipoUsuario.id == 1:
            libros_vendidos = []
            data = {
                'titulo': "Libros Vendidos",
                'libros_vendidos': libros_vendidos,
            }
        else:
            libros_comprados = []
            data = {
                'titulo':'Libros Comprados',
                'libros_comprados':libros_comprados
            }
        return render_template('index.html', data=data)
    else:
        return redirect(url_for('login'))

@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(None, request.form['email'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado:
            login_user(usuario_logeado)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Session cerrada exitosamente')
    return redirect(url_for('login'))

@app.route('/libros')
@login_required
def listaLibros():
    data = {
        'libros':ModeloLibro.listadoDeLibros(db)
    }
    return render_template('libros.html', data=data)

def pagina_no_encontrada(error):
    return render_template('errors/404.html'), 404

def pagina_no_autorizada(error):
    return redirect(url_for('login'))

def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, pagina_no_autorizada)
    app.register_error_handler(404, pagina_no_encontrada)
    
    return app