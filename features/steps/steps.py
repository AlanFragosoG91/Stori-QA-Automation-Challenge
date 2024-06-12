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

@when('I select option {option} in the dropdown')
def step_impl(context, option):
    dropdown = Select(context.driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]'))
    dropdown.select_by_index(int(option))

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
    context.driver.save_screenshot('screenshotTest.png')
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
    courses = context.driver.find_elements(By.XPATH, '//td[contains(text(), "$25")]/preceding-sibling::td[1]')
    for course in courses:
        print(course.text)

@then('I print the courses that cost $15')
def step_impl(context):
    courses = context.driver.find_elements(By.XPATH, '//td[contains(text(), "$15")]/preceding-sibling::td[1]')
    for course in courses:
        print(course.text)

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
    iframe = context.driver.find_element(By.XPATH, '//iframe[@id="courses-iframe"]')
    context.driver.switch_to.frame(iframe)
    text = context.driver.find_element(By.XPATH, '//h1')
    print(text.text)
    context.driver.switch_to.default_content()

@then('I close the browser')
def step_impl(context):
    context.driver.quit()