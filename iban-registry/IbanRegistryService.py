
import pandas as pd


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
    def convertir_txt_a_excel(archivo_txt, archivo_excel): 
        
        
        try:
            print(f" Leyendo archivo: {archivo_txt}")
            
            # PASO 1: Leer el archivo TXT
            # Intentamos diferentes encodings comunes hasta encontrar el correcto
            encodings = ['latin-1', 'cp1252', 'iso-8859-1', 'utf-8']
            df = None
            
            for encoding in encodings:
                try:
                    print(f"   Intentando con encoding: {encoding}")
                    df = pd.read_csv(
                        archivo_txt,
                        sep='\t',
                        encoding=encoding,
                        keep_default_na=False
                    )
                    print(f"   ✓ Encoding correcto: {encoding}")
                    break
                except UnicodeDecodeError:
                    continue
            
            if df is None:
                raise Exception("No se pudo detectar el encoding del archivo")
            
            print(f" Archivo leído correctamente")
            print(f"   - Filas: {len(df)}")
            print(f"   - Columnas: {len(df.columns)}")
            
            # PASO 2: Guardar a Excel
            # - index=False evita que se guarde la columna de índice numérico
            # - engine='openpyxl' es el motor para crear archivos .xlsx
            print(f"\n Guardando en Excel: {archivo_excel}")
            df.to_excel(archivo_excel, index=False, engine='openpyxl')
            
            print(f" ¡Conversión completada exitosamente!")
            print(f"   Archivo guardado: {archivo_excel}")
            
            return True
            
        except FileNotFoundError:
            print(f" ERROR: No se encontró el archivo '{archivo_txt}'")
            print(f"   Verifica que el archivo existe y el nombre es correcto")
            return False
            
        except Exception as e:
            print(f" ERROR durante la conversión: {str(e)}")
            return False