from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


DB = PostgresEngine(
    config={
        "database": "grimorios",
        "user": "postgres",
        "password": "f9sjav6k5k",
        "host": "localhost",
        "port": 5432,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["database.piccolo_app", "database_data.piccolo_app"]
)
