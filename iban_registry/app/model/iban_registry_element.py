from pydantic import BaseModel
from typing import Optional

class IBANRegistryElement(BaseModel):
    name_of_country: Optional[str] = None
    iban_prefix_country_code_iso: Optional[str] = None
    country_code_includes_other_countries_territories: Optional[str] = None
    sepa_country: Optional[str] = None
    sepa_country_also_includes: Optional[str] = None
    domestic_account_number_example: Optional[str] = None