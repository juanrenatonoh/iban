
import pandas as pd
from fastapi import  UploadFile, File
from ..db.iban_registry_repository import IbanRegistryRepository
import io

class RegistryService:

    def __init__(self):
        self.repository = IbanRegistryRepository()
    


    '''
    Valida las columnas del Data element en el registry
    '''
    def validate_data_element(self,data: dict):

        REQUIRED_FIELDS = [
                "Name of country",
                "IBAN prefix country code (ISO 3166)",
                "Country code includes other countries/territories",
                "SEPA country",
                "SEPA country also includes",
                "Domestic account number example",
                "BBAN",
                "BBAN structure",
                "BBAN length",
                "Bank identifier position within the BBAN",
                "Bank identifier pattern",
                "Branch identifier position within the BBAN",
                "Branch identifier pattern",
                "Bank identifier example",
                "Branch identifier example",
                "BBAN example",
                "IBAN",
                "IBAN structure",
                "IBAN length",
                "Effective date",
                "IBAN electronic format example",
                "IBAN print format example",
                "Contact details",
                "Organisation",
                "Department",
                "Street Address",
                "City / Postcode",
                "Department (generic) Email",
                "Department Tel",
                "Primary Contact",
                "Name",
                "First Name",
                "Title",
                "Email",
                "Tel",
                "Secondary Contact",
                "Name",
                "First Name",
                "Title",
                "Email",
                "Tel",
                "Updates",
                "Last update date",
        ]

            
        if "Data element" not in data:
            raise Exception("Archivo no valido  , no se encontro la fila Data element")

        values = [v for v in data["Data element"].values() if v not in ("", None)]

        if len(values) != len(REQUIRED_FIELDS):
            raise Exception(f"El número de columnas del Data element es invalido. "f"Esperado: {len(REQUIRED_FIELDS)}, recibido: {len(values)}."
                )

        for expected, actual in zip(REQUIRED_FIELDS, values):
            if actual != expected:
                raise Exception(f"Columna Data element invalida :  '{expected}' pero se recibió '{actual}'.")

        return


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
        
        self.validate_data_element(registros)
        # Validar que las cabeceras sean correctas
        
        
        
        #for clave,valor in data_element.items():
        #    print(clave,valor)
        
        # self.repository.insertar_varios(registros)
        return True
            

    

    