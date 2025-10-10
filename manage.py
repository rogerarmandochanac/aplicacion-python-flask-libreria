from app import inicializar_app
from config import config

app = inicializar_app(config['development'])

if __name__ == '__main__':
    app.run()