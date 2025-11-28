from fastapi import APIRouter, File, UploadFile


router = APIRouter()

@router.get("/",summary="hello world")
async def root():
    return {"message": "Hello World"}


@router.post("/upload",summary="Upload the IBAN Registry int txt format provided by swift with the ISO 13616 standard")
async def upload_registry(file: UploadFile = File(...)):
    
    # IbanRegistryService.upload_registry(file)
    
    return {
        "exito": True,
        "mensaje": "Proceso finalizado" 
    }
    
