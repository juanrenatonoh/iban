from pydantic import BaseModel
from typing import Optional

class IBANRegistryBBAN(BaseModel):
    bban: Optional[str] = None
    bban_structure: Optional[str] = None
    bban_length: Optional[str] = None
    bank_identifier_position_within_the_bban: Optional[str] = None
    bank_identifier_pattern: Optional[str] = None
    branch_identifier_position_within_the_bban: Optional[str] = None
    branch_identifier_pattern: Optional[str] = None
    bank_identifier_example: Optional[str] = None
    branch_identifier_example: Optional[str] = None
    bban_example: Optional[str] = None