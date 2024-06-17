from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class EstatusTable(Table, tablename="estatus_table", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class GrimorioTable(Table, tablename="grimorio_table", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class SolicitudTable(Table, tablename="solicitud_table", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2024-06-16T15:36:17:355550"
VERSION = "1.11.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="database", description=DESCRIPTION
    )

    manager.add_table(
        class_name="AsignacionTable",
        tablename="asignacion_table",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="GrimorioTable",
        tablename="grimorio_table",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="EstatusTable",
        tablename="estatus_table",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="SolicitudTable",
        tablename="solicitud_table",
        schema=None,
        columns=None,
    )

    manager.add_column(
        table_class_name="AsignacionTable",
        tablename="asignacion_table",
        column_name="solicitud_id",
        db_column_name="solicitud_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": SolicitudTable,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": "id",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="AsignacionTable",
        tablename="asignacion_table",
        column_name="estatus_id",
        db_column_name="estatus_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": EstatusTable,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": "id",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="AsignacionTable",
        tablename="asignacion_table",
        column_name="grimorio_id",
        db_column_name="grimorio_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": GrimorioTable,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": "id",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="GrimorioTable",
        tablename="grimorio_table",
        column_name="nombre",
        db_column_name="nombre",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="GrimorioTable",
        tablename="grimorio_table",
        column_name="rareza",
        db_column_name="rareza",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="EstatusTable",
        tablename="estatus_table",
        column_name="estatus",
        db_column_name="estatus",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 200,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="SolicitudTable",
        tablename="solicitud_table",
        column_name="nombre",
        db_column_name="nombre",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="SolicitudTable",
        tablename="solicitud_table",
        column_name="apellido",
        db_column_name="apellido",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="SolicitudTable",
        tablename="solicitud_table",
        column_name="identificacion",
        db_column_name="identificacion",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 10,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="SolicitudTable",
        tablename="solicitud_table",
        column_name="edad",
        db_column_name="edad",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="SolicitudTable",
        tablename="solicitud_table",
        column_name="afinidad_magica",
        db_column_name="afinidad_magica",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
