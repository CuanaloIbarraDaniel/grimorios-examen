import json
from models.solicitudmodel import SolicitudModel
from database.tables import (SolicitudTable, AsignacionTable)


# GET /solicitudes: Consulta todas las solicitudes.
async def ObtenerTodasSolicitudes():
    _SolicitudModel = json.load(await SolicitudTable.select())
    _SolicitudModelList = []

    for _Solicitud in _SolicitudModel:
        _SolicitudModelList.append(SolicitudModel(
            id = _Solicitud['id'],
            nombre = _Solicitud['nombre'],
            apellido = _Solicitud['apellido'],
            identificacion = _Solicitud['identificacion'],
            edad = _Solicitud['edad'],
            afinidad_magica = _Solicitud['afinidad_magica'])
    )

    return _SolicitudModelList


# By Id
async def ObtenerByIdSolicitudes(_SolicitudId: int):
    _SolicitudModel = json.load(await SolicitudTable.select().where(SolicitudTable.id == _SolicitudId))

    return SolicitudModel(
        id = _SolicitudModel['id'],
        nombre = _SolicitudModel['nombre'],
        apellido = _SolicitudModel['apellido'],
        identificacion = _SolicitudModel['identificacion'],
        edad = _SolicitudModel['edad'],
        afinidad_magica = _SolicitudModel['afinidad_magica'],
    )


# POST /solicitud: Envía solicitud de ingreso.
async def CrearSolicitud(_SolcitudModel: SolicitudModel):
    _solicitudModelId = await SolicitudTable.insert(SolicitudTable(
        nombre = _SolcitudModel.nombre, 
        apellido = _SolcitudModel.apellido,
        identificacion = _SolcitudModel.identificacion,
        edad = _SolcitudModel.edad,
        afinidad_magica = _SolcitudModel.afinidad_magica   
    )).returning(SolicitudTable.id)

    return await ObtenerByIdSolicitudes(_solicitudModelId)


# PUT /solicitud/{id}: Actualiza solicitud de ingreso. 
async def ActualizarSolicitud(_SolicitudId: int, _SolcitudModel: SolicitudModel):
    _SolicitudModelId = await SolicitudTable.update({ 
        SolicitudTable.nombre: _SolcitudModel.nombre, 
        SolicitudTable.apellido: _SolcitudModel.apellido,
        SolicitudTable.identificacion: _SolcitudModel.identificacion,
        SolicitudTable.edad: _SolcitudModel.edad,
        SolicitudTable.afinidad_magica: _SolcitudModel.afinidad_magica
    }).where(SolicitudTable.id == _SolicitudId).returning(SolicitudTable.id)
    
    return await ObtenerByIdSolicitudes(_SolicitudModelId)


# PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
async def ParchearSolicitud(_SolicitudId: int, _estatus: int):
    _SolicitudModelId = await AsignacionTable.update({
        AsignacionTable.estatus_id: _estatus
    }).where(AsignacionTable.solicitud_id == _SolicitudId).returning(SolicitudTable.id)
    
    return await ObtenerByIdSolicitudes(_SolicitudModelId)


# DELETE /solicitud/{id}: Elimina solicitud de ingreso.
async def EliminarSolicitudes(_id: int):
    await AsignacionTable.delete().where(AsignacionTable.solicitud_id == _id)
    await SolicitudTable.delete().where(SolicitudTable.id == _id)
    return _id