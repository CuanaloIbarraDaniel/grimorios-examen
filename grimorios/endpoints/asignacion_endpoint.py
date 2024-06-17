import json
from models.asignacionmodel import AsignacionModel
from database.tables import (SolicitudTable, AsignacionTable)


# GET /asignaciones: Consulta asignaciones de Grimorios.
async def ObtenerTodasAsignaciones():
    _AsignacionModel = json.load(await AsignacionTable.select(
        AsignacionTable.id,
        AsignacionTable.solicitud_id,
        AsignacionTable.solicitud_id.name,
        AsignacionTable.solicitud_id.apellido,
        AsignacionTable.estatus_id, 
        AsignacionTable.estatus_id.estatus, 
        AsignacionTable.grimorio_id, 
        AsignacionTable.grimorio_id.nombre))
    
    print(_AsignacionModel)

    return AsignacionModel()