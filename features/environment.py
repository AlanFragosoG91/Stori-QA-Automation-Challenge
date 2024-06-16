from selenium import webdriver
import os

def before_all(context):
     # Configuración de Appium para Android
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",  # Reemplazar con el ID del dispositivo/emulador
        "app": "/path/to/your/app.apk",  # Reemplazar con la ruta a tu aplicación
        "automationName": "UiAutomator2"
    }
    
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

 # Para iOS,
        # Configuración de Appium para iPhone
    # desired_caps = {
    #     "platformName": "iOS",
    #     "deviceName": "iPhone Simulator",
    #     "platformVersion": "14.4",  # Reemplazar con la versión de iOS
    #     "app": "/path/to/your/app.app",  # Reemplazar con la ruta a tu aplicación
    #     "automationName": "XCUITest"
    # }
    
    #Asegurarnos que la carpeta 'reports' existe antes de ejecutar y sino existe, crearla.
    reports_dir = 'reports' 
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

def after_all(context):
    """
    Ejecutado una vez después de que todas las pruebas hayan terminado.
    Aquí se puede limpiar recursos que se configuraron en before_all.
    """
    context.driver.quit()  # Cerrar el navegador

def before_scenario(context, scenario):
    """
    Ejecutado antes de cada escenario de prueba.
    Aquí se pueden restablecer estados que deberían estar listos antes de cada prueba.
    """
    context.driver.reset()

def after_scenario(context, scenario):
    """
    Ejecutado después de cada escenario de prueba.
    Aquí se pueden limpiar o registrar los resultados del escenario.
    """
    if scenario.status == "failed":
        # Tomar una captura de pantalla en caso de fallo
        context.driver.save_screenshot(f"screenshots/{scenario.name}.png")
        

def before_step(context, step):
    """
    Ejecutado antes de cada paso.
    Aquí se puede hacer seguimiento detallado de los pasos.
    """
    pass  # No se realiza ninguna acción en este ejemplo

def after_step(context, step):
    """
    Ejecutado después de cada paso.
    Aquí se puede registrar o verificar el estado de cada paso.
    """
    pass  # No se realiza ninguna acción en este ejemplo

def before_tag(context, tag):
    """
    Ejecutado antes de un escenario o característica con un tag específico.
    Aquí se pueden configurar cosas específicas basadas en tags.
    """
    if tag == "database":
        # Configuración específica si el escenario está marcado con "database"
        pass

def after_tag(context, tag):
    """
    Ejecutado después de un escenario o característica con un tag específico.
    Aquí se pueden limpiar cosas específicas basadas en tags.
    """
    if tag == "database":
        # Limpieza específica si el escenario está marcado con "database"
        pass