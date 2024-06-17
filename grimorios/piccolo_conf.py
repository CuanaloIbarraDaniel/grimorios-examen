from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry
from settings import _AppSetting


DB = PostgresEngine(
    config={
        "database": _AppSetting.DatabaseName,
        "user": _AppSetting.DatabaseUsername,
        "password": _AppSetting.DatabasePassword,
        "host": _AppSetting.DatabaseHost,
        "port": _AppSetting.DatabasePort,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["database.piccolo_app", "database_data.piccolo_app"]
)
