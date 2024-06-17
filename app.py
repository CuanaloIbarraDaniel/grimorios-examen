import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from Models.AsignacionModel import AsignacionModel
from Models.EstatusModel import EstatusModel
from Models.SolicitudModel import SolicitudModel
from endpoints.asignacion_endpoint import ObtenerTodasAsignaciones
from endpoints.estatus_endpoint import ObtenerTodosEstados
from endpoints.solicitud_endpoint import ActualizarSolicitud, CrearSolicitud, EliminarSolicitudes, ObtenerTodasSolicitudes, ParchearSolicitud


app = FastAPI(
    routes=[
        Mount("/static/", StaticFiles(directory="static")),
    ],
)


# TaskModelIn: t.Any = create_pydantic_model(table=Task, model_name="TaskModelIn")
# TaskModelOut: t.Any = create_pydantic_model(
#     table=Task, include_default_columns=True, model_name="TaskModelOut"
# )


# POST /solicitud: Envía solicitud de ingreso.
@app.post("/solicitud", response_model=SolicitudModel)
async def get_solicitudes(_SolicitudModel: SolicitudModel):
    return await CrearSolicitud(_SolicitudModel)


# PUT /solicitud/{id}: Actualiza solicitud de ingreso.
@app.put("/solicitudes/{_SolicitudId}", response_model=SolicitudModel)
async def put_solicitudes(_SolicitudId, _SolicitudModel: SolicitudModel):
    return await ActualizarSolicitud(_SolicitudId, _SolicitudModel)


# PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
@app.patch("/solicitudes/{_SolicitudId}/estatus", response_model=SolicitudModel)
async def patch_solicitudes(_SolicitudId: int, _estatus: int):
    return await ParchearSolicitud(_SolicitudId, _estatus)


# GET /solicitudes: Consulta todas las solicitudes.
@app.get("/solicitudes", response_model=t.List[SolicitudModel])
async def get_solicitudes():
    return await ObtenerTodasSolicitudes()


# GET /asignaciones: Consulta asignaciones de Grimorios.
@app.get("/asignaciones", response_model=t.List[AsignacionModel])
async def get_asignaciones():
    return await ObtenerTodasAsignaciones()

@app.get("/estatus", response_model=t.List[EstatusModel])
async def get_estatus():
    return await ObtenerTodosEstados()


# DELETE /solicitud/{id}: Elimina solicitud de ingreso. 
@app.delete("/solicitudes/{id}")
async def get_solicitudes(id: int):
    return await EliminarSolicitudes()





# @app.get("/tasks/", response_model=t.List[TaskModelOut])
# async def tasks():
#     return await Task.select().order_by(Task.id)


# @app.post("/tasks/", response_model=TaskModelOut)
# async def create_task(task_model: TaskModelIn):
#     task = Task(**task_model.dict())
#     await task.save()
#     return task.to_dict()


# @app.put("/tasks/{task_id}/", response_model=TaskModelOut)
# async def update_task(task_id: int, task_model: TaskModelIn):
#     task = await Task.objects().get(Task.id == task_id)
#     if not task:
#         return JSONResponse({}, status_code=404)

#     for key, value in task_model.dict().items():
#         setattr(task, key, value)

#     await task.save()

#     return task.to_dict()


# @app.delete("/tasks/{task_id}/")
# async def delete_task(task_id: int):
#     task = await Task.objects().get(Task.id == task_id)
#     if not task:
#         return JSONResponse({}, status_code=404)

#     await task.remove()

#     return JSONResponse({})


# @app.on_event("startup")
# async def open_database_connection_pool():
#     try:
#         engine = engine_finder()
#         await engine.start_connection_pool()
#     except Exception:
#         print("Unable to connect to the database")


# @app.on_event("shutdown")
# async def close_database_connection_pool():
#     try:
#         engine = engine_finder()
#         await engine.close_connection_pool()
#     except Exception:
#         print("Unable to connect to the database")
