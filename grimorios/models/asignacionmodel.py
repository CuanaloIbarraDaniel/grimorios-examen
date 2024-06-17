class AsignacionModel():
    id: int
    solicitud_id: int
    solicitud_nombre: str
    estatus_id: int
    estatus_nombre: str
    grimorio_id: int
    grimorio_nombre: str

    def __init__(self, id, solicitud_id, estatus_id, grimorio_id, solicitud_nombre="", estatus_nombre="", grimorio_nombre="") -> None:
        self.id = id
        self.solicitud_id = solicitud_id
        self.solicitud_nombre = solicitud_nombre
        self.estatus_id = estatus_id
        self.estatus_nombre = estatus_nombre
        self.grimorio_id = grimorio_id
        self.grimorio_nombre = grimorio_nombre

    def __repr__(self):
        return f'{str(self.id)}, {str(self.solicitud_id)}, {str(self.solicitud_nombre)}, {str(self.estatus_id)}, {str(self.estatus_nombre)}, {str(self.grimorio_id)}, {str(self.grimorio_nombre)}'