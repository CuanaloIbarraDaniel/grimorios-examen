class SolicitudModel():
    id: int
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad_magica: str

    def __init__(self, id, nombre, apellido, identificacion, edad, afinidad_magica) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.edad = edad
        self.afinidad_magica = afinidad_magica

    def __repr__(self):
        return f'{str(self.id)}, {str(self.nombre)}, {str(self.apellido)}, {str(self.identificacion)}, {str(self.edad)}, {str(self.afinidad_magica)}'