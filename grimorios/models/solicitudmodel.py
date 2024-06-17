from typing import Annotated
from pydantic import BaseModel, Field

class SolicitudModel(BaseModel):
    id: int
    nombre: Annotated[str, Field(strict=True, max_length=20, pattern=r'')]
    apellido: Annotated[str, Field(strict=True, max_length=20)]
    identificacion: Annotated[str, Field(strict=True, max_length=10)]
    edad: Annotated[int, Field(strict=True)]
    afinidad_magica: Annotated[str, Field(pattern=r'\b(Oscuridad|Luz|Fuego|Agua|Viento|Tierra)\b')]

    def __init__(self, id, nombre, apellido, identificacion, edad, afinidad_magica) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.edad = edad
        self.afinidad_magica = afinidad_magica