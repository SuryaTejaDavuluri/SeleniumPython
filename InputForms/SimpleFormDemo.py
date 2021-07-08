from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# driver = webdriver.Chrome()
browser = "chrome"
if browser == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    raise Exception("Check the driver")

driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/")
print(driver.title)

time.sleep(5)
driver.find_element(By.ID, 'at-cv-lightbox-close').click()

driver.find_element(By.LINK_TEXT, 'Input Forms').click()
driver.find_element(By.LINK_TEXT, 'Simple Form Demo').click()

buttons = driver.find_elements(By.XPATH, '//button[@type="button" and @class="btn btn-default"]')


def single_input_field(value):
    driver.find_element(By.ID, 'user-message').send_keys(value)
    for i in buttons:
        print(i.text)
        if i.text == 'Show Message':
            i.click()
    x = driver.find_element(By.ID, 'display').text
    print(x)
    if x == value:
        print('Text Matched')
    else:
        print("Text MisMatched")


def two_input_field(value1, value2):
    driver.find_element(By.ID, 'sum1').send_keys(value1)
    driver.find_element(By.ID, 'sum2').send_keys(value2)
    for j in buttons:
        if j.text == 'Get Total':
            j.click()
    y = int(driver.find_element(By.ID, 'displayvalue').text)
    print(y)
    if y == int(value1)+int(value2):
        print('Value Matched')
    else:
        print("Value MisMatched")


single_input_field("Hello 1234")
two_input_field(30, 40)

time.sleep(10)
driver.quit()
