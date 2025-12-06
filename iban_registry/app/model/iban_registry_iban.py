from pydantic import BaseModel
from typing import Optional

class IBANRegistryIBAN(BaseModel):
    iban: Optional[str] = None
    iban_structure: Optional[str] = None
    iban_length: Optional[str] = None
    effective_date: Optional[str] = None
    iban_electronic_format_example: Optional[str] = None
    iban_print_format_example: Optional[str] = None