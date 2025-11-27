# 📊 IBAN Registry 


## ⚠️ Aviso sobre el estado del proyecto

[![Status: Under Development](https://img.shields.io/badge/status-under_development-yellow)]()
[![WIP](https://img.shields.io/badge/work_in_progress-yes-orange)]()

Gracias por el interés en este repositorio.  
El proyecto se encuentra actualmente en **desarrollo activo**, por lo que es posible que la implementación presente diferencias respecto a la documentación disponible.  
Las estructuras, módulos y funcionalidades pueden cambiar sin previo aviso mientras se estabiliza la arquitectura.


## 📖 Descripción

Este proyecto convierte el archivo de texto del **Registro Internacional de IBAN** (International Bank Account Number) a formato Excel para facilitar su análisis y consulta.

El registro IBAN contiene información estandarizada sobre la estructura de cuentas bancarias internacionales de aproximadamente **89 países**.

---

## 🚀 Instalación y Uso

### Requisitos

Ubicarse en el directorio del proyecto iban-registry

```bash
cd iban-registry
```

Si no existe el entorno virtual venv crearlo con el siguiente comando

```bash
python3 -m venv venv
```

Activar el entorno virtual

Linux/Mac

```bash
source venv/bin/activate
```

Windows

```powershell
.\venv\Scripts\activate
```

Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Ejecución
```bash
python3 main.py
```

### Resultado
Se generará un archivo `registro_iban.xlsx` con todos los datos estructurados.

---

## 📁 Estructura del Archivo Original

El documento TXT contiene una tabla transpuesta donde:
- **Las columnas representan países** (aproximadamente 89)
- **Las filas representan atributos** (información sobre cada país)
- **Separador**: Tabulador (`\t`)
- **Encoding**: Latin-1 / Windows-1252 , (Considerar que el archivo original es en Windows si lo descargas desde el sitio web oficial puede afectar tu s.o igual es contemplado utf8)

---

## 📋 Diccionario de Datos

A continuación se describe cada fila del archivo y su significado:

### 🌍 Información General del País

| # | Campo | Descripción | Ejemplo |
|---|-------|-------------|---------|
| 1 | **Name of country** | Nombre oficial del país | `Spain`, `Mexico`, `Germany` |
| 2 | **IBAN prefix country code** | Código ISO 3166 de 2 letras | `ES`, `MX`, `DE` |
| 3 | **Country code includes other countries/territories** | Territorios adicionales cubiertos por el mismo código | `N/A` o lista de códigos |
| 4 | **SEPA country** | Si el país pertenece a la zona SEPA | `Yes` / `No` |
| 5 | **SEPA country also includes** | Territorios SEPA adicionales | `N/A` o lista |

---

### 💳 Estructura de Cuentas Bancarias (BBAN)

**BBAN** = Basic Bank Account Number (número de cuenta nacional sin el código de país)

| # | Campo | Descripción | Ejemplo |
|---|-------|-------------|---------|
| 6 | **Domestic account number example** | Ejemplo de número de cuenta nacional | `00000001212453611324` |
| 7 | **BBAN structure** | Estructura del BBAN con notación especial | `4!n4!n1!n1!n10!n` |
| 8 | **BBAN length** | Longitud total del BBAN en caracteres | `20`, `24`, `16` |

#### 📝 Notación de Estructura BBAN
- `n` = dígito numérico (0-9)
- `a` = letra mayúscula (A-Z)
- `c` = carácter alfanumérico (A-Z, 0-9)
- `!` = longitud fija
- Número antes de `!` = cantidad de caracteres

**Ejemplos:**
- `4!n` = 4 dígitos numéricos fijos
- `8!c` = 8 caracteres alfanuméricos fijos
- `2!a` = 2 letras mayúsculas fijas

---

### 🏦 Identificadores Bancarios

| # | Campo | Descripción | Ejemplo |
|---|-------|-------------|---------|
| 9 | **Bank identifier position** | Posición del código bancario dentro del BBAN | `1-4` (del carácter 1 al 4) |
| 10 | **Bank identifier pattern** | Patrón del identificador bancario | `4!n`, `3!n` |
| 11 | **Branch identifier position** | Posición del código de sucursal | `5-8` o `N/A` |
| 12 | **Branch identifier pattern** | Patrón del identificador de sucursal | `4!n` o vacío |
| 13 | **Bank identifier example** | Ejemplo real de código bancario | `2100`, `0081` |
| 14 | **Branch identifier example** | Ejemplo real de código de sucursal | `0418` o vacío |
| 15 | **BBAN example** | Ejemplo completo del BBAN | `21000418450200051332` |

---

### 🔢 Estructura de IBAN Completo

**IBAN** = Código de país (2 letras) + Dígitos de control (2 números) + BBAN

| # | Campo | Descripción | Ejemplo |
|---|-------|-------------|---------|
| 16 | **IBAN structure** | Estructura completa del IBAN | `ES2!n4!n4!n1!n1!n10!n` |
| 17 | **IBAN length** | Longitud total del IBAN | `24`, `22`, `20` |
| 18 | **Effective date** | Fecha desde la cual es válido | `Apr-07`, `Jan-12` |
| 19 | **IBAN electronic format example** | IBAN sin espacios (para sistemas) | `ES9121000418450200051332` |
| 20 | **IBAN print format example** | IBAN con espacios (para humanos) | `ES91 2100 0418 4502 0005 1332` |

---

### 🏢 Información de Contacto Institucional

| # | Campo | Descripción |
|---|-------|-------------|
| 21 | **Organisation** | Organización responsable del registro (Banco Central, Asociación Bancaria) |
| 22 | **Department** | Departamento específico dentro de la organización |
| 23 | **Street Address** | Dirección postal completa |
| 24 | **City / Postcode** | Ciudad y código postal |
| 25 | **Department Email** | Correo electrónico de contacto |
| 26 | **Department Tel** | Número telefónico de contacto |

---

### 👤 Contactos Principales y Secundarios

#### Contacto Principal (Filas 27)
- **Name** - Apellido del contacto
- **First Name** - Nombre del contacto
- **Title** - Cargo o título
- **Email** - Correo electrónico directo
- **Tel** - Teléfono directo

#### Contacto Secundario (Filas 28)
- Misma estructura que el contacto principal
- Persona alternativa para consultas

---

### 📅 Metadatos

| # | Campo | Descripción | Ejemplo |
|---|-------|-------------|---------|
| 29 | **Last update date** | Fecha de última actualización del registro | `Oct-25`, `Mar-21` |

---

## 📊 Ejemplo de Uso del Excel Generado

Una vez convertido a Excel, puedes:

### 🔍 Buscar información de un país
1. Filtrar por columna "Name of country"
2. Ver todas las filas con información de ese país

### 📈 Análisis de datos
- Contar cuántos países tienen IBAN de 24 caracteres
- Listar todos los países SEPA
- Comparar estructuras BBAN entre países

### 🔗 Validaciones
- Verificar la estructura correcta de un IBAN
- Obtener ejemplos de formato para pruebas
- Consultar longitudes permitidas

---

## 🌐 ¿Qué es IBAN?

**IBAN** (International Bank Account Number) es un estándar internacional para identificar cuentas bancarias de manera única.

### Estructura General
```
ES91 2100 0418 4502 0005 1332
│ │  └─────────────────────┘
│ │            └─ BBAN (Basic Bank Account Number)
│ └─ Dígitos de control (2 números)
└─ Código de país ISO 3166 (2 letras)
```

### Ventajas
✅ Reduce errores en transferencias internacionales  
✅ Facilita pagos automáticos en zona SEPA  
✅ Estándar reconocido mundialmente  
✅ Incluye validación mediante dígitos de control  

---

## 📚 Referencias

- **SWIFT**: Gestiona el registro oficial de IBAN
- **ISO 13616**: Estándar internacional para IBAN
- **SEPA**: Single Euro Payments Area (Zona Única de Pagos en Euros)

---

## 🛠️ Solución de Problemas

### Error de encoding
```
❌ 'utf-8' codec can't decode byte...
```
**Solución**: El script detecta automáticamente el encoding correcto (latin-1, cp1252, etc.)

### Archivo no encontrado
```
❌ No se encontró el archivo
```
**Solución**: Verifica que el archivo TXT esté en la misma carpeta que el script


## 📝 Notas Adicionales

- **N/A**: Indica que el campo no aplica para ese país
- **Campos vacíos**: Algunos países no tienen sucursales (Branch identifier)
- **SEPA**: Solo países europeos + algunos territorios
- **Actualización**: Los datos se actualizan periódicamente (ver "Last update date")

---

## 📄 Licencia

Licencia del Software
Este proyecto está licenciado bajo la Licencia MIT.

Los datos del registro IBAN son propiedad de SWIFT y están disponibles públicamente para consulta.

Fuente oficial: 

https://www.swift.com/es/node/301396

https://www.swift.com/swift-resource/11971/download

https://www.swift.com/swift-resource/9606/download



Este software solo proporciona una herramienta de conversión de formato. Los datos en sí pertenecen a SWIFT y están sujetos a sus términos de uso.

---
## Autores

* **Juan Renato Noh** - [Juan Renato Noh](www.linkedin.com/in/juanrenatonoh)

---

**Última actualización de esta documentación**: Noviembre 2024
