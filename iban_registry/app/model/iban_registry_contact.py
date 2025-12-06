from pydantic import BaseModel
from typing import Optional

class IBANRegistryContact(BaseModel):
    priority: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None
    tel: Optional[str] = None