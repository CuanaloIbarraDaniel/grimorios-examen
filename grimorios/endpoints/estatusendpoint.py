import json
from database.tables import (EstatusTable)
from models.estatusmodel import EstatusModel


# Obtener todos los estados
async def ObtenerTodosEstados():
    _EstatusModel = await EstatusTable.select()
    _EstatusModelList = []

    for _Estatus in _EstatusModel:
        _EstatusModelList.append(EstatusModel(
            id = _Estatus['id'],
            estatus = _Estatus['estatus'])
        )
    return _EstatusModelList


async def ObtenerPorNombreEstatus(_Estatus: str):
    _EstatusModel = await EstatusTable.select().where(EstatusTable.estatus == _Estatus)
    _EstatusModel = _EstatusModel[0]
    return EstatusModel(
        id = _EstatusModel['id'],
         estatus = _EstatusModel['estatus']
    )