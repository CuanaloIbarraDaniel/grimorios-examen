from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry
from settings import _AppSetting
from piccolo_conf import *

DB = PostgresEngine(
    config={
        "database": _AppSetting.DatabaseNameTest,
        "user": _AppSetting.DatabaseUsername,
        "password": _AppSetting.DatabasePassword,
        "host": _AppSetting.DatabaseHost,
        "port": _AppSetting.DatabasePort,
    }
)