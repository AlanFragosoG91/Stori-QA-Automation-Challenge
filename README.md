# Stori-QA-Automation-Challenge
Este proyecto utiliza Behave junto con Appium para automatizar pruebas de aplicaciones móviles en dispositivos Android e iOS.

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
2. **Appium Server**: Descarga e instala Appium desde [Appium](http://appium.io/).
3. **Android SDK**: Para pruebas en Android, asegúrate de tener el SDK de Android instalado y configurado.
4. **Xcode**: Para pruebas en iOS, asegúrate de tener Xcode instalado y configurado.
5. **Dispositivo o Emulador**: Configura un dispositivo físico o emulador de Android/iOS.


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

4. **Configurar `features/environment.py`**: Asegúrate de que las capacidades deseadas (desired capabilities) en el archivo `environment.py` estén configuradas correctamente para tu dispositivo/emulador y aplicación.


## Ejecución de pruebas

1. **Navegar a la carpeta del proyecto:**
    ```bash
    cd behave project
    ```
2. **Iniciar el servidor de Appium**:
    ```bash
    appium

2. **Ejecutar las pruebas con Behave**
    ```bash
    behave -f behave_html_formatter:HTMLFormatter -o reports/TestExecution.html
    ```

## Notas

1. Asegúrate de reemplazar "emulator-5554" y "/path/to/your/app.apk" con los valores correctos para tu dispositivo/emulador y aplicación.

2. Las rutas y los selectores XPath en steps.py deben ser ajustados según la estructura real del DOM de tu aplicación móvil.