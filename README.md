# pre-entrega-automation-testing-carlosconde# 🧪 Proyecto de QA Automation - Sauce Demo

Proyecto de automatización de pruebas para practicar y familiarizarse con Selenium WebDriver y pytest, utilizando el sitio de pruebas [Sauce Demo](https://www.saucedemo.com/).

## 📋 Descripción

Este proyecto tiene como propósito:

- Familiarizarse con las pruebas de automatización web
- Aprender a seleccionar e interactuar con elementos del DOM
- Practicar el uso de Selenium WebDriver
- Generar reportes HTML de las pruebas ejecutadas

## 🛠️ Tecnologías Utilizadas

- **Python** - Lenguaje de programación
- **Selenium** - Framework para automatización de navegadores web
- **WebDriver** - Controlador para interactuar con el navegador
- **pytest** - Framework de testing
- **pytest-html** - Plugin para generar reportes HTML

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior instalado
- Google Chrome instalado (o el navegador de tu preferencia)

### Instalar Dependencias

```bash
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager
```

## 📁 Estructura del Proyecto

```
proyecto-qa-automation/
├── tests/
│   ├── conftest.py          # Configuración de fixtures
│   ├── test_login.py        # Pruebas de login
│   ├── test_inventory.py    # Pruebas de inventario
│   └── test_cart.py         # Pruebas del carrito
├── utils/
│   └── login.py             # Funciones auxiliares
├── run_test.py              # Script para ejecutar las pruebas
└── README.md
```

## 🚀 Ejecución de Pruebas

### Ejecutar todas las pruebas

```bash
python run_test.py
```

## 📊 Reportes

Después de ejecutar las pruebas, se generará un archivo `report.html` en la raíz del proyecto con los resultados detallados de todas las pruebas ejecutadas.

Para visualizar el reporte:

1. Abrir el archivo `report.html` en tu navegador
2. Revisar los resultados, tiempos de ejecución y capturas de errores

## 🔑 Credenciales de Prueba

Para el sitio [Sauce Demo](https://www.saucedemo.com/):

- **Usuario:** `standard_user`
- **Contraseña:** `secret_sauce`

## 📝 Casos de Prueba Incluidos

- ✅ Login exitoso
- ✅ Visualización del inventario de productos
- ✅ Agregar productos al carrito
- ✅ Navegación al carrito de compras

## 🤝 Contribuciones

Este es un proyecto de práctica personal. Siéntete libre de hacer fork y adaptarlo a tus necesidades.

## 📄 Licencia

Este proyecto es de uso educativo y de práctica.
