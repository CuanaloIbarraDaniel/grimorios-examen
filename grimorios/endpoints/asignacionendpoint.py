import json
from models.asignacionmodel import AsignacionModel
from database.tables import (AsignacionTable, SolicitudTable)


# GET /asignaciones: Consulta asignaciones de Grimorios.
async def ObtenerTodasAsignaciones():

    _AsignacionModel = await AsignacionTable.raw("SELECT astb.id, astb.solicitud_id, astb.estatus_id, astb.grimorio_id, concat_ws(' ', sotb.nombre, sotb.apellido) as solicitud_nombre, estb.estatus AS estatus_nombre, grtb.nombre AS grimorio_nombre FROM asignacion_table AS astb INNER JOIN solicitud_table AS sotb ON astb.solicitud_id = sotb.id INNER JOIN estatus_table AS estb ON astb.estatus_id = estb.id INNER JOIN grimorio_table AS grtb ON astb.grimorio_id = grtb.id")
    _AsignacionModelList = []

    for _Asignacion in _AsignacionModel:
        _AsignacionModelList.append(AsignacionModel(
            id = _Asignacion['id'],
            solicitud_id = _Asignacion['solicitud_id'],
            solicitud_nombre = _Asignacion['solicitud_nombre'],
            estatus_id = _Asignacion['estatus_id'],
            estatus_nombre = _Asignacion['estatus_nombre'],
            grimorio_id = _Asignacion['grimorio_id'],
            grimorio_nombre = _Asignacion['grimorio_nombre']
        ))

    return _AsignacionModelList


async def CrearAsignacion(_AsignacionModel: AsignacionModel):
    _AsignacionId = await AsignacionTable.insert(AsignacionTable(
        solicitud_id = _AsignacionModel.solicitud_id, 
        estatus_id = _AsignacionModel.estatus_id,
        grimorio_id = _AsignacionModel.grimorio_id 
    )).returning(AsignacionTable.id)
    _AsignacionId = _AsignacionId[0]["id"]
    return await ObtenerByIdAsignacion(_AsignacionId)


# By Id
async def ObtenerByIdAsignacion(_AsignacionId: int):
    _SolicitudModel = await AsignacionTable.select().where(AsignacionTable.id == _AsignacionId)
    _SolicitudModel = _SolicitudModel[0]
    return AsignacionModel(
        id = _SolicitudModel['id'],
        solicitud_id = _SolicitudModel['solicitud_id'],
        estatus_id = _SolicitudModel['estatus_id'],
        grimorio_id = _SolicitudModel['grimorio_id']
    )