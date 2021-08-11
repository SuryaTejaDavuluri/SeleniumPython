from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import xlrd
import pytest

browser = "edge"
if browser == "chrome":
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
elif browser == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    raise Exception("Check the driver")

wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/")
print(driver.title)
popup = wait.until(ec.visibility_of_element_located((By.ID, 'at-cv-lightbox-close')))
popup.click()

driver.find_element(By.LINK_TEXT, 'Input Forms').click()
driver.find_element(By.LINK_TEXT, 'Simple Form Demo').click()

buttons = driver.find_elements(By.XPATH, '//button[@type="button" and @class="btn btn-default"]')


def test_single_input_field(value):
    driver.find_element(By.ID, 'user-message').clear()
    driver.find_element(By.ID, 'user-message').send_keys(value)
    for i in buttons:
        # print(i.text)
        if i.text == 'Show Message':
            i.click()
    x = driver.find_element(By.ID, 'display').text
    print(x)
    if x == value:
        print('Text Matched')
    else:
        print("Text MisMatched")


def test_two_input_field(value1, value2):
    driver.find_element(By.ID, 'sum1').clear()
    driver.find_element(By.ID, 'sum1').send_keys(value1)
    driver.find_element(By.ID, 'sum2').clear()
    driver.find_element(By.ID, 'sum2').send_keys(value2)
    for j in buttons:
        if j.text == 'Get Total':
            j.click()
    y = int(driver.find_element(By.ID, 'displayvalue').text)
    print(y)
    if y == int(value1) + int(value2):
        print('Value Matched')
    else:
        print("Value MisMatched")


workbook = xlrd.open_workbook("/TestData/testdata.xlsx")
sheet = workbook.sheet_by_name("SimpleDemo")

rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    simpleInput = sheet.cell_value(curr_row, 0)
    twoInputA = sheet.cell_value(curr_row, 1)
    twoInputB = sheet.cell_value(curr_row, 2)

    test_single_input_field(simpleInput)
    test_two_input_field(twoInputA, twoInputB)

# driver.get_screenshot_as_file('pic2.png')

S = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('pic1.png')
driver.quit()
