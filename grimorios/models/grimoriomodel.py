class GrimorioModel():
    id: int
    nombre: str
    rareza: int

    def __init__(self, id, nombre, rareza) -> None:
        self.id = id
        self.nombre = nombre
        self.rareza = rareza

    def __repr__(self):
        return f'{str(self.id)}, {str(self.nombre)}, {str(self.rareza)}'