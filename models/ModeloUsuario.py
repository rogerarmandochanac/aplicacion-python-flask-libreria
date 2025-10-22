from werkzeug.security import check_password_hash
from .entities.TipoUsuario import TipoUsuario
from .entities.Usuario import Usuario
class ModeloUsuario:

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = f"""
            SELECT id, usuario, password FROM usuario WHERE usuario = '{usuario.usuario}';
            """
            cursor.execute(sql)
            data = cursor.fetchone()
            coincide = check_password_hash(data[2], usuario.password)
            if coincide:
                usuario = Usuario(data[0], data[1], None, None)
                return usuario
            else:
                None
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = f"""
            SELECT USU.id, USU.usuario, TIP.id, TIP.nombre 
            FROM usuario USU JOIN tipoUsuario TIP ON USU.tipoUsuario_id = TIP.id
            WHERE USU.id = {id};
            """
            cursor.execute(sql)
            data = cursor.fetchone()
            print(data)
            tipoUsuario = TipoUsuario(data[2], data[3])
            usuario_logeado = Usuario(data[0], data[1], None, tipoUsuario)
            return usuario_logeado
        except Exception as e:
            raise Exception(e)