from piccolo.columns import Varchar, Integer, UUID, ForeignKey
from piccolo.table import Table



class SolicitudTable(Table):
    id = UUID(),
    nombre = Varchar(length=20)
    apellido = Varchar(length=20)
    identificacion = Varchar(length=10)
    edad = Integer()
    afinidad_magica = Varchar(length=20)



class GrimorioTable(Table):
    id = UUID(),
    nombre = Varchar(length=20)
    rareza = Integer()



class EstatusTable(Table):
    id = UUID(),
    estatus = Varchar(length=200)



class AsignacionTable(Table):
    id = UUID(),
    solicitud_id = ForeignKey(references=SolicitudTable, target_column=SolicitudTable.id)
    estatus_id = ForeignKey(references=EstatusTable, target_column=EstatusTable.id)
    grimorio_id = ForeignKey(references=GrimorioTable, target_column=GrimorioTable.id)