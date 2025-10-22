from .entities.Libro import Libro
from .entities.Autor import Autor
class ModeloLibro:
    @classmethod
    def listadoDeLibros(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT lib.isbn, lib.titulo, lib.ano_edicion, aut.nombres, aut.apellidos, lib.precio 
                    FROM libro lib JOIN autor aut 
                    ORDER BY titulo ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            libros = []
            for row in data:
                aut = Autor(id=None, nombres=row[3], apellidos=row[4])
                libro = Libro(row[0], row[1], aut, row[2], precio=None)
                libros.append(libro)
            return libros
        except Exception as e:
            raise Exception(e)