class EstatusModel():
    id: int
    estatus: str

    def __init__(self, id, estatus) -> None:
        self.id = id
        self.estatus = estatus