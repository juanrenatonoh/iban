from IbanRegistryService import IbanRegistryService


# ==========================================
# CONFIGURACIÓN
# ==========================================

# Nombre del archivo de entrada
ARCHIVO_ENTRADA = 'iban-registry.txt'

# Nombre del archivo de salida
ARCHIVO_SALIDA = 'registro_iban.xlsx'

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

print("=" * 60)
print("CONVERSOR IBAN TXT → EXCEL")
print("=" * 60)
print()

exito = IbanRegistryService.convertir_txt_a_excel(ARCHIVO_ENTRADA, ARCHIVO_SALIDA);

print()
print("=" * 60)

if exito:
    print("PROCESO FINALIZADO ✓")
else:
    print("PROCESO FINALIZADO CON ERRORES ✗")
    
print("=" * 60)
    
  