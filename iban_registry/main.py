from fastapi import FastAPI

from .core.app_logger import logger
from .routers import registrys

app = FastAPI()
app.include_router(registrys.router,tags=["iban_registry"],prefix="/registry")


