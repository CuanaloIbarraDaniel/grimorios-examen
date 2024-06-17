import typing as t

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import FastAPIError, RequestValidationError, ValidationException
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from models.solicitudviewmodel import SolicitudViewModel
from models.asignacionmodel import AsignacionModel
from models.estatusmodel import EstatusModel
from models.solicitudmodel import SolicitudModel
from endpoints.asignacionendpoint import ObtenerTodasAsignaciones
from endpoints.estatusendpoint import ObtenerTodosEstados
from endpoints.solicitudendpoint import ActualizarSolicitud, CrearSolicitud, EliminarSolicitudes, ObtenerTodasSolicitudes, ParchearSolicitud


app = FastAPI()
origins = ['http://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TaskModelIn: t.Any = create_pydantic_model(table=Task, model_name="TaskModelIn")
# TaskModelOut: t.Any = create_pydantic_model(
#     table=Task, include_default_columns=True, model_name="TaskModelOut"
# )

@app.get("/")
def read_root():
    return {"Hello": "World"}



# POST /solicitud: Envía solicitud de ingreso.
@app.post("/solicitud")
async def get_solicitudes(_SolicitudViewModel: SolicitudViewModel):    
    return await CrearSolicitud(_SolicitudViewModel)



# PUT /solicitud/{id}: Actualiza solicitud de ingreso.
@app.put("/solicitud/{_SolicitudId}")
async def put_solicitudes(_SolicitudId: int, _SolicitudViewModel: SolicitudViewModel):
    return await ActualizarSolicitud(_SolicitudId, _SolicitudViewModel)



# PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
@app.patch("/solicitud/{_SolicitudId}/estatus")
async def patch_solicitudes(_SolicitudId: int, SolicitudEstatus: int):
    return await ParchearSolicitud(_SolicitudId, SolicitudEstatus)



# GET /solicitudes: Consulta todas las solicitudes.
@app.get("/solicitudes")
async def get_solicitudes():
    return await ObtenerTodasSolicitudes()



# GET /asignaciones: Consulta asignaciones de Grimorios.
@app.get("/asignaciones")
async def get_asignaciones():
    return await ObtenerTodasAsignaciones()



@app.get("/estatus")
async def get_estatus():
    return await ObtenerTodosEstados()



# DELETE /solicitud/{id}: Elimina solicitud de ingreso. 
@app.delete("/solicitud/{_SolicitudId}")
async def get_solicitudes(_SolicitudId: int):
    return await EliminarSolicitudes(_SolicitudId)



# @app.exception_handler(ValueError)
# async def value_error_exception_handler(request: Request, exc: ValueError):
#     return JSONResponse(status_code=exc.status_code, content={{"mensaje": str(exc)})

@app.exception_handler(StarletteHTTPException)
async def starlette_http_exception(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detalles": str(exc)})

@app.exception_handler(RequestValidationError)
async def request_validation_error(request, exc):
    for error in exc.errors(): 
        error['message'] = error.pop('msg')
    return JSONResponse(content=jsonable_encoder({"detalles": exc.errors()}), status_code=status.HTTP_400_BAD_REQUEST)

@app.exception_handler(ValidationException)
async def validation_exception(request, exc):
    return JSONResponse(status_code=exc.status.HTTP_400_BAD_REQUEST, content={"detalles": str(exc)})

@app.exception_handler(FastAPIError)
async def fast_api_error(request, exc):
    return JSONResponse(status_code=exc.status.HTTP_400_BAD_REQUEST, content={"detalles": str(exc)})

@app.exception_handler(TypeError)
async def type_error(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detalles": str(exc)})



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
