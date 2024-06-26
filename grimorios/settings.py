import enum

class LogLevel(str, enum.Enum):  # noqa: WPS600
    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"

class Settings():
    Host: str = "127.0.0.1"
    Port: int = 8470
    # quantity of workers for uvicorn
    WorkersCount: int = 1
    # Enable uvicorn reloading
    Reload: bool = True
    # Current environment
    Environment: str = "dev"
    AppLogLevel: LogLevel = LogLevel.INFO
    # Variables for the database
    DatabaseHost: str = "localhost"
    DatabasePort: int = 5432
    DatabaseUsername: str = ""
    DatabasePassword: str = ""
    DatabaseName: str = ""
    DatabaseNameTest: str = ""

_AppSetting = Settings()