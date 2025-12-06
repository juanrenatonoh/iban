
import pandas as pd
from fastapi import  UploadFile, File,Depends
from ..db.iban_registry_repository import IbanRegistryRepository
from ..model.iban_registry import IBANRegistry , IBANRegistryElement , IBANRegistryBBAN , IBANRegistryIBAN , IBANRegistryContactDetails , IBANRegistryUpdates , IBANRegistryContact
from ..core.domain_exception import DomainException
import io

class RegistryService:

    def __init__(self,iban_registry_repository: IbanRegistryRepository = Depends()):
        self.iban_registry_repository = iban_registry_repository

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
            raise DomainException("Archivo no valido  , no se encontro la fila Data element")

        values = [v for v in data["Data element"].values() if v not in ("", None)]

        if len(values) != len(REQUIRED_FIELDS):
            raise DomainException(f"El número de columnas del Data element es invalido. "f"Esperado: {len(REQUIRED_FIELDS)}, recibido: {len(values)}."
                )

        for expected, actual in zip(REQUIRED_FIELDS, values):
            if actual != expected:
                raise DomainException(f"Columna Data element invalida :  '{expected}' pero se recibió '{actual}'.")

        return

    '''
    Map the description pattern example to the iban registry entity
    '''
    def map_description_pattern_example_to_iban_registry(self,data: str):
        
        registry_list = []

        for clave, values in data.items():

            if clave == "Data element":
                continue
            
            
            registry = IBANRegistry(
                element=IBANRegistryElement(
                    name_of_country=values[0],
                    iban_prefix_country_code_iso=values[1],
                    country_code_includes_other_countries_territories=values[2],
                    sepa_country=values[3],
                    sepa_country_also_includes=values[4],
                    domestic_account_number_example=values[5],
                ),
                bban=IBANRegistryBBAN(
                    bban=values[6],
                    bban_structure=values[7],
                    bban_length=values[8],
                    bank_identifier_position_within_the_bban=values[9],
                    bank_identifier_pattern=values[10],
                    branch_identifier_position_within_the_bban=values[11],
                    branch_identifier_pattern=values[12],
                    bank_identifier_example=values[13],
                    branch_identifier_example=values[14],
                    bban_example=values[15],
                ),
                iban=IBANRegistryIBAN(
                    iban=values[16],
                    iban_structure=values[17],
                    iban_length=values[18],
                    effective_date=values[19],
                    iban_electronic_format_example=values[20],
                    iban_print_format_example=values[21],
                ),
                contact_details=IBANRegistryContactDetails(
                    organisation=values[23],
                    department=values[24],
                    street_address=values[25],
                    city_postcode=values[26],
                    department_generic_email=values[27],
                    department_tel=values[28],
                    contacts=[
                        IBANRegistryContact(
                            priority="primary",
                            name=values[30],
                            first_name=values[31],
                            title=values[32],
                            email=values[33],
                            tel=values[34],
                        ),
                        IBANRegistryContact(
                            priority="secondary",
                            name=values[36],
                            first_name=values[37],
                            title=values[38],
                            email=values[39],
                            tel=values[40],  
                        ),
                    ]
                ),
                updates=IBANRegistryUpdates(
                    last_update_date=values[42]
                )
            )

            registry_list.append(registry)

        return registry_list

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
            raise DomainException("No se pudo detectar el encoding del archivo")

        registros = df.to_dict("dict") 
        
        self.validate_data_element(registros)
        registry_list = self.map_description_pattern_example_to_iban_registry(registros)
        
        self.iban_registry_repository.delete_all()
        self.iban_registry_repository.save(registry_list)
        
        return True
            
    
    '''
    Find all records in the database
    '''
    def find_all(self):
        return self.iban_registry_repository.find_all()


    

    