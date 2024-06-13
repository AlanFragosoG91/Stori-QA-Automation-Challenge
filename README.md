# Stori-QA-Automation-Challenge
Este proyecto utiliza Behave, una herramienta de pruebas BDD (Behavior-Driven Development)

## Estructura del Proyecto

my_behave_project/
|-- features/
  |-- reports/
| |-- steps/
| | |-- steps.py
| |-- environment.py
| |-- automation.feature
|-- requirements.txt
|-- gitignore
|-- README.md

- **features/**: Carpeta que contiene los archivos `.feature`, los pasos (`steps`) asociados y el reporte (`reports`) con el estatus de todos los casos de prueba
- **features/steps/**: Carpeta que contiene los archivos de implementación de los pasos (`steps.py`).
- **features/environment.py**: Archivo para la configuración global del entorno de pruebas.
- **features/automation.feature**: Archivo que contiene los escenarios desarrollados en Gherkin.
- **requirements.txt**: Archivo que lista las dependencias del proyecto.
- **README.md**: Archivo descriptivo del repositorio

## Pre-requisitos

1. **Python 3.x**: Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Chrome WebDriver**: Descarga el Chrome WebDriver compatible con la versión de tu navegador Chrome desde [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) y asegúrate de que esté en tu PATH.

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/AlanFragosoG91/Stori-QA-Automation-Challenge.git
    cd my_behave_project
    ```

2. **Crear un entorno virtual** (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de pruebas

1. **Navegar a la carpeta del proyecto:**
    ```bash
    cd behave project
    ```
2. **Ejecutar las pruebas con Behave**
    ```bash
    behave -f behave_html_formatter:HTMLFormatter -o reports/TestExecution.html
    ```
