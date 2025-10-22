class Autor:
    def __init__(self, id, nombres, apellidos, fechaNacimiento=None):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento

        @property
        def getNombreCompleto(self):
            return f"{self.nombres} {self.apeliidos}"