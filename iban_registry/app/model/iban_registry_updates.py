from pydantic import BaseModel
from typing import Optional


class IBANRegistryUpdates(BaseModel):
    last_update_date: Optional[str] = None  