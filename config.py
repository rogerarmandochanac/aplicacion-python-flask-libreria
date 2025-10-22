class Config:
    SECRET_KEY = 'DQWIDHsedre120-3213NSN!@@!*()'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'gonzo007'
    MYSQL_DB = 'flask_libreria'

class DevelopmentConfig(Config):
    DEBUG=True

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig,
}