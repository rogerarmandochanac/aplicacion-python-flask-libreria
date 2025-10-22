from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, usuario, password, tipoUsuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipoUsuario = tipoUsuario
    
    def create_password(password):
        hash_password = generate_password_hash(password)
        coincide = check_password_hash(hash_password, password)
        return coincide