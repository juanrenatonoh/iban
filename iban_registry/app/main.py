from fastapi import FastAPI

from .routers import registries

app = FastAPI()
app.include_router(registries.router,tags=["registry"],prefix="/registry")


