import json
from database.tables import (EstatusTable)
from models.estatusmodel import EstatusModel


# Obtener todos los estados
async def ObtenerTodosEstados():
    _EstatusModel = json.load(await EstatusTable.select())
    _EstatusModelList = []

    for _Estatus in _EstatusModel:
        _EstatusModelList.append(EstatusModel(
            id = _Estatus['id'],
            estatus = _Estatus['estatus'])
    )

    return _EstatusModelList