class EstatusModel():
    id: int
    estatus: str

    def __init__(self, id, estatus):
        self.id = id
        self.estatus = estatus

    def __repr__(self):
        return f'{str(self.id)}, {str(self.estatus)}'