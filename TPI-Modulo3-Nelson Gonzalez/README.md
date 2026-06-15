# Trabajo Práctico Integrador - Automatización de Pruebas

Proyecto integrador de automatización de testing, desarrollado con **Python**, **pytest** y **Selenium**. Incluye automatización de casos funcionales sobre un sitio web (SauceDemo) y validación de APIs REST (PokeAPI), con generación de reportes HTML.

## Índice

- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Casos de prueba - Sitio 1: SauceDemo](#casos-de-prueba---sitio-1-saucedemo)
- [Casos de prueba - Sitio 2: PokeAPI](#casos-de-prueba---sitio-2-pokeapi)
- [Ejercicios adicionales](#ejercicios-adicionales)
- [Cómo ejecutar los tests](#cómo-ejecutar-los-tests)
- [Generación de reportes HTML](#generación-de-reportes-html)
- [Notas y consideraciones](#notas-y-consideraciones)

---

## Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| **Python 3.13** | Lenguaje base del proyecto |
| **pytest** | Framework de testing y ejecución de casos |
| **pytest-html** | Generación de reportes HTML de resultados |
| **Selenium** | Automatización del navegador (Sitio 1 - SauceDemo) |
| **requests** | Consumo y validación de API REST (Sitio 2 - PokeAPI) |
| **ChromeDriver** | Driver para controlar Google Chrome |

---

## Estructura del proyecto

```
TPI-modulo3/
│
├── Caso1_EJ3.py        # Sitio 1 - Caso 1: Ordenar productos por precio
├── Caso2_EJ3.py        # Sitio 1 - Caso 2: Carrito y validaciones de checkout
├── Caso3_EJ3.py        # Sitio 1 - Caso 3: Flujo completo de compra
│
├── Sitio2_EJ1.py       # Sitio 2 - API: Validación de datos de berry/1
├── Sitio2_EJ2.py       # Sitio 2 - API: Comparación entre berry/1 y berry/2
├── Sitio2_EJ3.py       # Sitio 2 - API: Validación de datos de Pikachu
│
├── Cuadratica.py       # Ejercicio adicional: resolución de ecuaciones cuadráticas
├── Numeros_Primos.py   # Ejercicio adicional: verificación de números primos
│
├── reportes/           # Carpeta donde se generan los reportes HTML
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Archivos/carpetas ignorados por git
└── README.md           # Este archivo
```

---

## Requisitos previos

- Python 3.10 o superior
- Google Chrome instalado
- Git

---

## Instalación

### 1. Crear y activar entorno virtual

```bash
python -m venv venv
```

```bash
# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no existe `requirements.txt`, instalar manualmente:

```bash
pip install selenium pytest pytest-html requests
```

---

## Casos de prueba - Sitio 1: SauceDemo

**URL del sitio:** https://www.saucedemo.com/
**Usuario:** `standard_user`
**Contraseña:** `secret_sauce`

### Caso 1 - Ordenamiento de productos por precio (`Caso1_EJ3.py`)

**Objetivo:** verificar que el ordenamiento "Price (low to high)" funcione correctamente.

Pasos automatizados:
1. Login con usuario estándar.
2. Seleccionar la opción de orden "Price (low to high)".
3. Obtener los precios de todos los productos listados.
4. Verificar que la lista de precios esté ordenada de menor a mayor.

### Caso 2 - Carrito y validaciones del formulario de checkout (`Caso2_EJ3.py`)

**Objetivo:** validar que todos los productos puedan agregarse al carrito y que el formulario de checkout muestre los errores correctos ante campos incompletos.

Pasos automatizados:
1. Login con usuario estándar.
2. Agregar todos los productos al carrito (6 productos).
3. Ir al carrito y verificar que contenga los 6 productos.
4. Ir a checkout.
5. Completar solo el nombre y presionar "Continue" → verificar error **"Error: Last Name is required"**.
6. Completar el apellido y presionar "Continue" → verificar error **"Error: Postal Code is required"**.

### Caso 3 - Flujo completo de compra (`Caso3_EJ3.py`)

**Objetivo:** validar el flujo end-to-end de agregar, remover y comprar productos.

Pasos automatizados:
1. Login con usuario estándar.
2. Agregar un producto al carrito.
3. Ir al carrito y remover el producto agregado.
4. Verificar que el carrito esté vacío (0 productos).
5. Volver al catálogo con "Continue Shopping".
6. Agregar 2 productos al carrito.
7. Verificar que el carrito contenga exactamente 2 productos.
8. Completar el checkout con nombre, apellido y código postal.
9. Finalizar la compra.
10. Verificar el mensaje de confirmación **"Thank you for your order!"**.

---

## Casos de prueba - Sitio 2: PokeAPI

**URL base:** https://pokeapi.co/api/v2/

### Caso 1 - Validación de datos de Berry (`Sitio2_EJ1.py`)

Consulta el endpoint `berry/1` y valida:
- Código de respuesta `200`.
- `size` igual a `20`.
- `soil_dryness` igual a `15`.
- `firmness.name` igual a `"soft"`.

### Caso 2 - Comparación entre Berries (`Sitio2_EJ2.py`)

Consulta `berry/1` y `berry/2`, y valida:
- `firmness.name` de berry/2 sea `"super-hard"`.
- `size` de berry/2 sea mayor al de berry/1.
- `soil_dryness` de berry/2 sea igual al de berry/1.

### Caso 3 - Validación de datos de Pikachu (`Sitio2_EJ3.py`)

Consulta `pokemon/pikachu` y valida:
- Código de respuesta `200`.
- `base_experience` esté entre 10 y 1000.
- El tipo del Pokémon sea `"electric"`.

---

## Ejercicios adicionales

Ejercicios de práctica con Python puro, sin testing automatizado.

### Ecuación cuadrática (`Cuadratica.py`)

Solicita al usuario los coeficientes **a**, **b** y **c**, calcula el discriminante y muestra el resultado según corresponda:
- Dos soluciones reales (discriminante > 0).
- Una única solución (discriminante = 0).
- Sin soluciones reales (discriminante < 0).

Ejecución:

```bash
python Cuadratica.py
```

### Números primos (`Numeros_Primos.py`)

Solicita al usuario un número y verifica si es primo, recorriendo los posibles divisores entre 2 y el número ingresado.

Ejecución:

```bash
python Numeros_Primos.py
```

---

## Cómo ejecutar los tests

### Ejecutar un caso puntual

```bash
pytest Caso1_EJ3.py -v -s
```

### Ejecutar todos los tests del proyecto

```bash
pytest -v -s
```

- `-v` → modo detallado (verbose), muestra cada test ejecutado.
- `-s` → muestra los `print()` definidos dentro de los tests.

---

## Generación de reportes HTML

Cada test puede ejecutarse generando su propio reporte HTML:

```bash
pytest Caso1_EJ3.py -v -s --html=reportes/caso1_ej3.html --self-contained-html
pytest Caso2_EJ3.py -v -s --html=reportes/caso2_ej3.html --self-contained-html
pytest Caso3_EJ3.py -v -s --html=reportes/caso3_ej3.html --self-contained-html

pytest Sitio2_EJ1.py -v -s --html=reportes/sitio2_ej1.html --self-contained-html
pytest Sitio2_EJ2.py -v -s --html=reportes/sitio2_ej2.html --self-contained-html
pytest Sitio2_EJ3.py -v -s --html=reportes/sitio2_ej3.html --self-contained-html
```

O bien, generar un único reporte con todos los tests del proyecto:

```bash
pytest -v -s --html=reportes/reporte_general.html --self-contained-html
```

- `--html=<ruta>` → indica dónde se guarda el reporte.
- `--self-contained-html` → genera el reporte en un solo archivo, sin dependencias externas (CSS/JS embebidos).

---

## Notas y consideraciones

- Los tests del **Sitio 1** abren Google Chrome en modo incógnito mediante `ChromeOptions`, con notificaciones y el aviso de "guardar contraseña" deshabilitados.
- Los tests del **Sitio 2** no requieren navegador, ya que se comunican directamente con la API mediante la librería `requests`.
- La carpeta `venv/` y los archivos de caché (`__pycache__/`, `.pytest_cache/`) **no deben subirse al repositorio**; están incluidos en `.gitignore`.
- Los reportes HTML generados se almacenan en la carpeta `reportes/`.
