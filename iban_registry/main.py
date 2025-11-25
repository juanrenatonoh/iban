from .IbanRegistryService import IbanRegistryService
from fastapi import FastAPI ,UploadFile, File
from .app_logger import logger
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

"""
Load the IBAN registry file
See the Dictionary file on Readme.md from the IBAN Registry
"""
@app.post("/upload_registry")
async def upload_registry(file: UploadFile = File(...)):
    
    logger.info("Uploading Iban Registry...")
    IbanRegistryService.upload_registry(file)
    logger.info("Iban Registry loaded successfully")
    
    return {
        "exito": True,
        "mensaje": "Proceso finalizado" 
    }
    


