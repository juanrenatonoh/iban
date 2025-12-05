
import pandas as pd
from fastapi import  UploadFile, File
from ..db.iban_registry_repository import IbanRegistryRepository
import io

class RegistryService:

    def __init__(self):
        self.repository = IbanRegistryRepository()

    
    """
    Upload the IBAN Registry int txt format provided by swift with the ISO 13616 standard
    """
    def upload_registry(self,file: UploadFile = File(...)): 

        print(f" Leyendo archivo:")
            
        # Detectar encoding y leer TXT
        encodings = ['latin-1', 'cp1252', 'iso-8859-1', 'utf-8']
        df = None
            
        for encoding in encodings:
            try:
                df = pd.read_csv(io.StringIO(file.file.read().decode(encoding)), sep='\t', keep_default_na=False)
                break
            except UnicodeDecodeError:
                continue

        if df is None:
            raise Exception("No se pudo detectar el encoding del archivo")

        registros = df.to_dict("dict") # analisis las cabeceras deben corresponder con la 0 hay que validar eso , y listo ya lo tenemos registrar desde la 1 hasta la 42 y listo :D 
        print(registros)
        # self.repository.insertar_varios(registros)
        return True
            
        


    