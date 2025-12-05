
import pandas as pd
from fastapi import  UploadFile, File
from ..db.iban_registry_repository import IbanRegistryRepository
import io

class RegistryService:

    def __init__(self):
        self.repository = IbanRegistryRepository()

    '''
    Validate the columns of the record Data element of the registry
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

    '''
    Map the description pattern example to the iban registry entity
    '''
    def map_description_pattern_example_to_iban_registry_entity(self,data: str):
        
        iban_registry = []

        for clave,values in data.items():
            
            if(clave == "Data element"):
                continue    
                
            iban_registry.append(
                        {
                            "name_of_country": values.get(0), 
                            "iban_prefix_country_code_iso": values.get(1),
                            "country_code_includes_other_countries_territories": values.get(2),
                            "sepa_country": values.get(3),
                            "sepa_country_also_includes": values.get(4),
                            "domestic_account_number_example": values.get(5),
                            "bban": values.get(6),
                            "bban_structure": values.get(7),
                            "bban_length": values.get(8),
                            "bank_identifier_position_within_the_bban": values.get(9),
                            "bank_identifier_pattern": values.get(10),
                            "branch_identifier_position_within_the_bban": values.get(11),
                            "branch_identifier_pattern": values.get(12),
                            "bank_identifier_example": values.get(13),
                            "branch_identifier_example": values.get(14),
                            "bban_example": values.get(15),
                            "iban": values.get(16),
                            "iban_structure": values.get(17),
                            "iban_length": values.get(18),
                            "effective_date": values.get(19),
                            "iban_electronic_format_example": values.get(20),
                            "iban_print_format_example": values.get(21),
                            "contact_details": values.get(22),
                            "organisation": values.get(23),
                            "department": values.get(24),
                            "street_address": values.get(25),
                            "city_postcode": values.get(26),
                            "department_generic_email": values.get(27),
                            "department_tel": values.get(28),
                            "primary_contact": values.get(29),
                            "name": values.get(30),
                            "first_name": values.get(31),
                            "title": values.get(32),
                            "email": values.get(33),
                            "tel": values.get(34),
                            "secondary_contact": values.get(35),
                            "name": values.get(36),
                            "first_name": values.get(37),
                            "title": values.get(38),
                            "email": values.get(39),
                            "tel": values.get(40),
                            "updates": values.get(41),
                            "last_update_date": values.get(42),
                        }
                    )

        return iban_registry

    '''
    Upload the IBAN Registry int txt format provided by swift with the ISO 13616 standard
    '''
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

        registros = df.to_dict("dict") 
        
        self.validate_data_element(registros)
        iban_registry = self.map_description_pattern_example_to_iban_registry_entity(registros)
        
        
        
        
        #for clave,valor in data_element.items():
        #    print(clave,valor)
        
        # self.repository.insertar_varios(registros)
        return True
            

    

    