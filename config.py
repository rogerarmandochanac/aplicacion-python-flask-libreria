class Config:
    SECRET_KEY = 'DQWIDHsedre120-3213NSN!@@!*()'

class DevelopmentConfig(Config):
    DEBUG=True

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig,
}