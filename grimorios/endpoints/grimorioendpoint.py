from database.tables import GrimorioTable
from models.grimoriomodel import GrimorioModel


async def ObtenerTodosGrimorios():
    _GrimorioModel = await GrimorioTable.select()
    _GrimorioModelList = []

    for _Grimorio in _GrimorioModel:
        _GrimorioModelList.append(GrimorioModel(
            id = _Grimorio['id'],
            nombre = _Grimorio['nombre'],
            rareza = _Grimorio['rareza']
    ))

    return _GrimorioModelList