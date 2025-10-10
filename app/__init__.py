from flask import (Flask, 
                   render_template, 
                   request,
                   redirect,
                   url_for
                   )
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['correo'])
        print(request.form['password'])
        return redirect(url_for('index'))
    return render_template('auth/login.html')

def pagina_no_encontrada(error):
    return render_template('errors/404.html'), 404

def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app