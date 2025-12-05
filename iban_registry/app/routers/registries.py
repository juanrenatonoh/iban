from fastapi import APIRouter, File, UploadFile, Depends,HTTPException
from ..services.registries_service import RegistryService


router = APIRouter()


@router.post("/upload",summary="Upload the IBAN Registry int txt format provided by swift with the ISO 13616 standard")
async def upload_registry(file: UploadFile = File(...),service: RegistryService = Depends()):
    
    try:
        service.upload_registry(file)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    
    return {
        "exito": True,
        "mensaje": "Proceso finalizado" 
    }
    
@router.get("/",summary="Get all records from Iban Registry")
async def find_all(service: RegistryService = Depends()):
    return service.find_all()