from IbanRegistryService import IbanRegistryService
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/importar_registry")
async def importar_registry():
    
    ARCHIVO_ENTRADA = 'iban-registry.txt'
    ARCHIVO_SALIDA = 'registro_iban.xlsx'

    print("=" * 60)
    print("CONVERSOR IBAN TXT → EXCEL")
    print("=" * 60)
    print()

    exito = IbanRegistryService.convertir_txt_a_excel(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)

    print()
    print("=" * 60)

    if exito:
        print("PROCESO FINALIZADO ✓")
    else:
        print("PROCESO FINALIZADO CON ERRORES ✗")
    
    print("=" * 60)

    return {
        "exito": exito,
        "mensaje": "Proceso finalizado" if exito else "Proceso finalizado con errores"
    }
    


