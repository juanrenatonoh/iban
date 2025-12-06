from pydantic import BaseModel
from .iban_registry_element import IBANRegistryElement
from .iban_registry_bban import IBANRegistryBBAN
from .iban_registry_iban import IBANRegistryIBAN
from .iban_registry_contact_details import IBANRegistryContactDetails
from .iban_registry_updates import IBANRegistryUpdates
from .iban_registry_contact import IBANRegistryContact

class IBANRegistry(BaseModel):
    data_element: IBANRegistryElement
    bban: IBANRegistryBBAN
    iban: IBANRegistryIBAN
    contact_details: IBANRegistryContactDetails
    updates: IBANRegistryUpdates
