from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
from datetime import datetime

from .routers import registries
from .core.domain_exception import DomainException

app = FastAPI()
app.include_router(registries.router,tags=["registry"],prefix="/registry")


@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=400,
        content={
            "timestamp": datetime.utcnow().isoformat(),
            "message": exc.message,
            "path": str(request.url)
        }
    )