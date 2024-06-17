"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig, table_finder
from .tables import (EstatusTable, GrimorioTable, SolicitudTable, AsignacionTable)


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="database",
    migrations_folder_path=os.path.join(
        CURRENT_DIRECTORY, "piccolo_migrations"
    ),
    table_classes=[EstatusTable, GrimorioTable, SolicitudTable, AsignacionTable],
    migration_dependencies=[],
    commands=[],
)
