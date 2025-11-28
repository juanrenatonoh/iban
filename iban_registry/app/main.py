from fastapi import FastAPI

from .core.app_logger import logger
from .routers import registries

app = FastAPI()
app.include_router(registries.router,tags=["registry"],prefix="/registry")


