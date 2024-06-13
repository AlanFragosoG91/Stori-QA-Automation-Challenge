from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@given('I open the browser and navigate to the automation practice page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://rahulshettyacademy.com/AutomationPractice/')

@when('I enter "{text}" and select "{country}"')
def step_impl(context, text, country):
    suggestion_box = context.driver.find_element(By.XPATH, '//input[@id="autocomplete"]')
    suggestion_box.send_keys(text)
    time.sleep(1)
    country_option = context.driver.find_element(By.XPATH, f'//li[contains(text(), "{country}")]')
    country_option.click()

@when('I select option 2 and then option 3 in the dropdown')
def step_impl(context):
    # Suponemos que el dropdown es el primer select en el formulario
    dropdown = context.driver.find_element(By.XPATH, '//form//select[1]')

    # Seleccionar opción 2
    option_2 = dropdown.find_element(By.XPATH, './option[2]')
    option_2.click()
    time.sleep(1)  # Pausa para ver el cambio

    # Seleccionar opción 3
    option_3 = dropdown.find_element(By.XPATH, './option[3]')
    option_3.click()
    time.sleep(1)  # Pausa para ver el cambio

@then('I should be able to see the change in the dropdown')
def step_impl(context):
    # Verificar que la opción 3 está seleccionada
    dropdown = context.driver.find_element(By.XPATH, '//form//select[1]')
    selected_option = dropdown.find_element(By.XPATH, './option[@selected]')
    assert selected_option == dropdown.find_element(By.XPATH, './option[3]')
    context.driver.quit()

@when('I click the Open Window button')
def step_impl(context):
    open_window_button = context.driver.find_element(By.XPATH, '//button[@id="openwindow"]')
    open_window_button.click()
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('I verify the 30 day money back guarantee text')
def step_impl(context):
    try:
        text_element = context.driver.find_element(By.XPATH, '//h2[contains(text(), "30 day Money Back Guarantee")]')
        assert "30 day Money Back Guarantee" in text_element.text
    except:
        context.driver.close()
        context.driver.switch_to.window(context.driver.window_handles[0])
        assert False

@when('I click the Open Tab button')
def step_impl(context):
    open_tab_button = context.driver.find_element(By.XPATH, '//a[@id="opentab"]')
    open_tab_button.click()
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('I scroll to the specific button and take a screenshot')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, '//span[contains(text(), "Login")]')
    context.driver.execute_script("arguments[0].scrollIntoView();", button)
    context.driver.save_screenshot('I scroll to the specific button and take a screenshot.png')
    context.driver.switch_to.window(context.driver.window_handles[0])

@when('I type "Stori Card" and click the Alert button')
def step_impl(context):
    alert_input = context.driver.find_element(By.XPATH, '//input[@id="name"]')
    alert_input.send_keys("Stori Card")
    alert_button = context.driver.find_element(By.XPATH, '//input[@id="alertbtn"]')
    alert_button.click()

@then('I verify and accept the alert text')
def step_impl(context):
    alert = context.driver.switch_to.alert
    assert "Hello Stori Card" in alert.text
    alert.accept()

@when('I type "Stori Card" and click the Confirm button')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH, '//input[@id="confirmbtn"]')
    confirm_button.click()

@then('I verify and accept the confirm text')
def step_impl(context):
    confirm = context.driver.switch_to.alert
    assert "Hello Stori Card, Are you sure you want to confirm?" in confirm.text
    confirm.accept()

@then('I print the courses that cost $25')
def step_impl(context):
    # Encontramos todas las celdas de precios en la tabla
    courses_25 = context.driver.find_elements(By.CSS_SELECTOR, 'table[name="courses"] td:nth-child(3)')
    count_25 = 0
    course_names_25 = []
    for price in courses_25:
        if price.text == "$25":
    # Navegamos a la celda anterior que contiene el nombre del curso  
            course_name = price.find_element(By.XPATH, './preceding-sibling::td[1]').text
            course_names_25.append(course_name)
    #Se agrega el nombre del curso a una lista reduciendo la sobrecarga de interacciones con el navegador y mejorando el rendimiento del script. "Append" se usa para acumular resulados de un bucle.
            count_25 += 1
    print(f"Number of courses that cost $25: {count_25}")
    print("Courses that cost $25:")
    for name in course_names_25:
        print(name)

@then('I print the courses that cost $15')
def step_impl(context):
     # Encontramos todas las celdas de precios en la tabla
    courses_15 = context.driver.find_elements(By.CSS_SELECTOR, 'table[name="courses"] td:nth-child(3)')
    count_15 = 0
    course_names_15 = []
    for price in courses_15:
        if price.text == "$15":
    # Navegamos a la celda anterior que contiene el nombre del curso        
            course_name = price.find_element(By.XPATH, './preceding-sibling::td[1]').text
            course_names_15.append(course_name)
    #Se agrega el nombre del curso a una lista reduciendo la sobrecarga de interacciones con el navegador y mejorando el rendimiento del script. "Append" se usa para acumular resulados de un bucle.
            count_15 += 1
    print(f"Number of courses that cost $15: {count_15}")
    print("Courses that cost $15:")
    for name in course_names_15:
        print(name)

@then('I print the names of all Engineers')
def step_impl(context):
    engineers = context.driver.find_elements(By.XPATH, '//td[text()="Engineer"]/preceding-sibling::td[1]')
    for engineer in engineers:
        print(engineer.text)

@then('I print the names of all Businessmans')
def step_impl(context):
    businessmen = context.driver.find_elements(By.XPATH, '//td[text()="Businessman"]/preceding-sibling::td[1]')
    for businessman in businessmen:
        print(businessman.text)

@then('I print the text highlighted in blue')
def step_impl(context):
    # Seleccionamos todas las filas de la tabla de cursos
    courses = context.driver.find_elements(By.XPATH, '//table[@name="courses"]/tbody/tr')
    
    # Recorremos las filas y imprimimos solo los índices impares
    for index, course in enumerate(courses):
        if index % 2 != 0:
            # Suponemos que el nombre del curso está en la primera celda
            course_name = course.find_element(By.XPATH, './td[1]').text
            print(f"Course at odd index {index}: {course_name}")

#@then('I close the browser')
#def step_impl(context):
#   context.driver.quit()