import typing as t

from fastapi import FastAPI, Query, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import FastAPIError, RequestValidationError, ValidationException
from fastapi.openapi.utils import get_openapi
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

# Los nombres y las descripciones para los tags
tags_metadata = [
    {
        "name": "Default",
        "description": "Operaciones creadas por default.",
    },
    {
        "name": "Solicitudes",
        "description": "Todas las operaciones relacionadas a las solicitudes de Grimorios.",
    },
    {
        "name": "Asignaciones",
        "description": "Operaciones relacionadas a las asignaciones que se relacionan a las tablas de Estatus y Grimorios.",
    },
    {
        "name": "Estatus",
        "description": "Maneja los Estatus de los Grimorios y Solicitudes.",
    },
]
# Inicializa el objeto de FastAPI
app = FastAPI(openapi_tags=tags_metadata)
# Middleware para garantizar que las llamadas lleguen al servicio
origins = ['http://localhost:8470']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# LLamada por default
@app.get("/", tags=["Default"])
def read_root():
    """
    Esta es la llamada por default del servidor y sirve para detectar si se puede alcanzar el mismo desde el exterior.
    """
    return {"Dev Screen"}



# POST /solicitud: Envía solicitud de ingreso.
@app.post("/solicitud", status_code=status.HTTP_200_OK, tags=["Solicitudes"])
async def get_solicitudes(_SolicitudViewModel: SolicitudViewModel):
    """
    Esta llamada se utiliza para poder crear solicitudes y asignaciones con una sola llamada.
    """
    return await CrearSolicitud(_SolicitudViewModel)



# PUT /solicitud/{id}: Actualiza solicitud de ingreso.
@app.put("/solicitud/{_SolicitudId}", status_code=status.HTTP_200_OK, tags=["Solicitudes"])
async def put_solicitudes(_SolicitudId: int, _SolicitudViewModel: SolicitudViewModel):
    """
    Esta llamada sirve para actualizar una solicitud usando una ID
    """
    return await ActualizarSolicitud(_SolicitudId, _SolicitudViewModel)



# PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
@app.patch("/solicitud/{_SolicitudId}/estatus", status_code=status.HTTP_200_OK, tags=["Solicitudes"])
async def patch_solicitudes(_SolicitudId: int, SolicitudEstatus: int):
    """
    Utilizado para actualizar el estatus de la solicitud (Se puede elegir entre Pendiente = 1, Aceptada = 2 y Rechazada = 3).
    """
    return await ParchearSolicitud(_SolicitudId, SolicitudEstatus)



# GET /solicitudes: Consulta todas las solicitudes.
@app.get("/solicitudes", status_code=status.HTTP_200_OK, tags=["Solicitudes"])
async def get_solicitudes():
    """    
    Esta llamada se utiliza para obtener todas las solicitudes que se encuentran en la base de datos
    """
    return await ObtenerTodasSolicitudes()



# DELETE /solicitud/{id}: Elimina solicitud de ingreso. 
@app.delete("/solicitud/{_SolicitudId}", status_code=status.HTTP_200_OK, tags=["Solicitudes"])
async def get_solicitudes(_SolicitudId: int):
    """
    Elimina una solicitud y su asignación correspondiente utilizando su ID
    """
    return await EliminarSolicitudes(_SolicitudId)



# GET /asignaciones: Consulta asignaciones de Grimorios.
@app.get("/asignaciones", status_code=status.HTTP_200_OK, tags=["Asignaciones"])
async def get_asignaciones():
    """
    Obtiene todas las asignaciones que se encuentran en la base de datos
    """
    return await ObtenerTodasAsignaciones()



@app.get("/estatus", status_code=status.HTTP_200_OK, tags=["Estatus"])
async def get_estatus():
    """
    OBtiene todos los estatus que se encuentran en la base de datos
    """
    return await ObtenerTodosEstados()




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



def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Swagger para Grimorios",
        version="1.1.0",
        summary="Este es un schema de OpenAPI",
        description="Schema para representar todas las operaciones posibles dentro de la API de Grimorios con la ayuda de OpenAPI",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi