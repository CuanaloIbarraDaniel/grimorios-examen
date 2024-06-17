import uvicorn
from settings import _AppSetting

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=_AppSetting.Host,
        port=_AppSetting.Port,
        reload=_AppSetting.Reload,
        log_level=_AppSetting.AppLogLevel.value.lower()
    )
