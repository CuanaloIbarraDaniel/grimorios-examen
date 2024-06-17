import json
import random
from endpoints.estatusendpoint import ObtenerPorNombreEstatus, ObtenerTodosEstados
from endpoints.grimorioendpoint import ObtenerTodosGrimorios
from endpoints.asignacionendpoint import CrearAsignacion
from models.solicitudviewmodel import SolicitudViewModel
from models.asignacionmodel import AsignacionModel
from models.estatusmodel import EstatusModel
from models.solicitudmodel import SolicitudModel
from database.tables import (SolicitudTable, AsignacionTable)


# GET /solicitudes: Consulta todas las solicitudes.
async def ObtenerTodasSolicitudes():
    _SolicitudModel = await SolicitudTable.select()
    _SolicitudModelList = []

    for _Solicitud in _SolicitudModel:
        _SolicitudModelList.append(SolicitudModel(
            id = _Solicitud['id'],
            nombre = _Solicitud['nombre'],
            apellido = _Solicitud['apellido'],
            identificacion = _Solicitud['identificacion'],
            edad = _Solicitud['edad'],
            afinidad_magica = _Solicitud['afinidad_magica']
    ))

    return _SolicitudModelList


# By Id
async def ObtenerByIdSolicitudes(_SolicitudId: int):
    _SolicitudModel = await SolicitudTable.select().where(SolicitudTable.id == _SolicitudId)
    _SolicitudModel = _SolicitudModel[0]
    return SolicitudModel(
        id = _SolicitudModel['id'],
        nombre = _SolicitudModel['nombre'],
        apellido = _SolicitudModel['apellido'],
        identificacion = _SolicitudModel['identificacion'],
        edad = _SolicitudModel['edad'],
        afinidad_magica = _SolicitudModel['afinidad_magica']
    )


# POST /solicitud: Envía solicitud de ingreso.
async def CrearSolicitud(_SolicitudVIewModel: SolicitudViewModel):
    _SolicitudModelId = await SolicitudTable.insert(SolicitudTable(
        nombre = _SolicitudVIewModel.nombre, 
        apellido = _SolicitudVIewModel.apellido,
        identificacion = _SolicitudVIewModel.identificacion,
        edad = _SolicitudVIewModel.edad,
        afinidad_magica = _SolicitudVIewModel.afinidad_magica
    )).returning(SolicitudTable.id)
    _SolicitudModelId = _SolicitudModelId[0]["id"]

    # Obtiene la solicitud creada en el comando anterior
    _SolicitudModel = await ObtenerByIdSolicitudes(_SolicitudModelId)
    # Obtiene el estatus por nombre
    _EstatusModel = await ObtenerPorNombreEstatus("Aceptada")
    # OBtiene todos los grimorios para que puedan ser utilizados en la eleccion con pesos
    _GrimorioModel = await ObtenerTodosGrimorios()

    _GrimorioModelId = []
    _GrimorioModelNombre = []
    _GrimorioModelRareza = []

    # # # Weighted choice
    for _Grimorio in _GrimorioModel:
        _GrimorioModelId.append(_Grimorio.id)
        _GrimorioModelNombre.append(_Grimorio.nombre)
        _GrimorioModelRareza.append(_Grimorio.rareza)

    _GrimorioId = random.choices(_GrimorioModelId, _GrimorioModelRareza, k=1)[0]

    await CrearAsignacion(AsignacionModel(0, _SolicitudModelId, _EstatusModel.id, _GrimorioId))

    return _SolicitudModel
    


# PUT /solicitud/{id}: Actualiza solicitud de ingreso. 
async def ActualizarSolicitud(_SolicitudId: int, _SolicitudVIewModel: SolicitudViewModel):
    _SolicitudModelId = await SolicitudTable.update({ 
        SolicitudTable.nombre: _SolicitudVIewModel.nombre, 
        SolicitudTable.apellido: _SolicitudVIewModel.apellido,
        SolicitudTable.identificacion: _SolicitudVIewModel.identificacion,
        SolicitudTable.edad: _SolicitudVIewModel.edad,
        SolicitudTable.afinidad_magica: _SolicitudVIewModel.afinidad_magica
    }).where(SolicitudTable.id == _SolicitudId).returning(SolicitudTable.id)
    _SolicitudModelId = _SolicitudModelId[0]["id"]
    return await ObtenerByIdSolicitudes(_SolicitudModelId)


# PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
async def ParchearSolicitud(_SolicitudId: int, _estatus: int):
    _SolicitudModelId = await AsignacionTable.update({
        AsignacionTable.estatus_id: _estatus
    }).where(AsignacionTable.solicitud_id == _SolicitudId).returning(SolicitudTable.id)

    _SolicitudModelId = _SolicitudModelId[0]["id"]
    return await ObtenerByIdSolicitudes(_SolicitudModelId)


# DELETE /solicitud/{id}: Elimina solicitud de ingreso.
async def EliminarSolicitudes(_SolicitudId: int):
    await AsignacionTable.delete().where(AsignacionTable.solicitud_id == _SolicitudId)
    await SolicitudTable.delete().where(SolicitudTable.id == _SolicitudId)
    return _SolicitudId