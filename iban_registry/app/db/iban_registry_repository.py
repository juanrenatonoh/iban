from .app_mongo_client import db
from ..model.registry import Registry

class IbanRegistryRepository:

    def __init__(self):
        self.collection = db["iban_registry"]

    '''
    Save list of iban registry in the database
    '''
    def save(self, iban_registry: list[Registry]):

        if not iban_registry:
            return 0
        
        records = [record.dict() for record in iban_registry]
        result = self.collection.insert_many(records)
        
        return len(records)

    '''
    Find all records in the database
    '''
    def find_all(self):
        records = self.collection.find({},{"_id":0}).to_list()
        return records
        