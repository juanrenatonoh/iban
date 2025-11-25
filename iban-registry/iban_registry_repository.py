from app_mongo_client import db


class IbanRegistryRepository:

    def __init__(self):
        self.collection = db["iban_registry"]

    def insertar_varios(self, datos: list[dict]):
        """
        Inserta múltiples documentos en la colección.
        datos: lista de diccionarios, cada diccionario es un registro.
        """
        if not datos:
            return {"inserted_count": 0}

        result = self.collection.insert_many(datos)
        
        return {"inserted_count": 10}