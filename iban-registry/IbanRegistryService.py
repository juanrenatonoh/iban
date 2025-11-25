
import pandas as pd
from fastapi import  UploadFile, File
from iban_registry_repository import IbanRegistryRepository



class IbanRegistryService:

    def __init__(self):
        pass

    """
        Convierte el archivo TXT del registro IBAN a formato Excel.
        
        Parámetros:
            archivo_txt (str): Ruta del archivo TXT de entrada
            archivo_excel (str): Ruta del archivo Excel de salida
        
        Retorna:
            bool: True si la conversión fue exitosa, False si hubo error
    """
    def upload_registry(file: UploadFile = File(...)): 
        
        ARCHIVO_ENTRADA = 'iban-registry.txt'
        ARCHIVO_SALIDA = 'registro_iban.xlsx'

        try:

            with open(ARCHIVO_ENTRADA, "wb") as f:
                f.write(file.file.read())

            print(f" Leyendo archivo:")
            
             # Detectar encoding y leer TXT
            encodings = ['latin-1', 'cp1252', 'iso-8859-1', 'utf-8']
            df = None

            for encoding in encodings:
                try:
                    df = pd.read_csv(ARCHIVO_ENTRADA, sep='\t', encoding=encoding, keep_default_na=False)
                    break
                except UnicodeDecodeError:
                    continue

            if df is None:
                raise Exception("No se pudo detectar el encoding del archivo")

            # Convertir cada fila a diccionario
            registros = df.to_dict(orient='records')
            repository = IbanRegistryRepository() 
            repository.insertar_varios(registros)
            return True
            
        except FileNotFoundError:
            print(f" ERROR: No se encontró el archivo ")
            print(f"   Verifica que el archivo existe y el nombre es correcto")
            return False
            
        except Exception as e:
            print(f" ERROR durante la conversión: {str(e)}")
            return False