from fastapi import APIRouter, File, UploadFile


router = APIRouter()

@router.get("/",summary="hello world")
async def root():
    return {"message": "Hello World"}


@router.post("/upload",summary="Upload the IBAN Registry int txt format provided by swift with the ISO 13616 standard")
async def upload_registry(file: UploadFile = File(...)):
    
    logger.info("Uploading Iban Registry...")
    # IbanRegistryService.upload_registry(file)
    logger.info("Iban Registry loaded successfully")
    
    return {
        "exito": True,
        "mensaje": "Proceso finalizado" 
    }
    
