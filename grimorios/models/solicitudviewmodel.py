from typing import Annotated
from pydantic import BaseModel, Field

class SolicitudViewModel(BaseModel):
    id: int
    nombre: Annotated[str, Field(strict=True, min_length=1, max_length=20, pattern=r'^[a-zA-z]+([\s][a-zA-Z]+)*$')]
    apellido: Annotated[str, Field(strict=True, min_length=1, max_length=20, pattern=r'^[a-zA-z]+([\s][a-zA-Z]+)*$')]
    identificacion: Annotated[str, Field(strict=True, min_length=1, max_length=10, pattern='^[a-zA-Z0-9]*$')]
    edad: Annotated[int, Field(strict=True, gt=0, lt=100)]
    afinidad_magica: Annotated[str, Field(pattern=r'\b(Oscuridad|Luz|Fuego|Agua|Viento|Tierra)\b')]

    def __repr__(self):
        return f'{str(self.id)}, {str(self.nombre)}, {str(self.apellido)}, {str(self.identificacion)}, {str(self.edad)}, {str(self.afinidad_magica)}'