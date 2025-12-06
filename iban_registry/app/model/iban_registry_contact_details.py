from typing import Optional, List
from .iban_registry_contact import IBANRegistryContact
from pydantic import BaseModel

class IBANRegistryContactDetails(BaseModel):
    organisation: Optional[str] = None
    department: Optional[str] = None
    street_address: Optional[str] = None
    city_postcode: Optional[str] = None
    department_generic_email: Optional[str] = None
    department_tel: Optional[str] = None
    contacts: Optional[List[IBANRegistryContact]] = None  # lista de contactos