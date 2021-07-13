from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = True

browser = "chrome"
if browser == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
elif browser == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    raise Exception("Check the driver")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/")
print(driver.title)
time.sleep(5)
driver.find_element(By.ID, 'at-cv-lightbox-close').click()

driver.find_element(By.LINK_TEXT, 'Input Forms').click()
driver.find_element(By.LINK_TEXT, 'Checkbox Demo').click()

# Single Checkbox
driver.find_element(By.ID, 'isAgeSelected').click()
if driver.find_element(By.ID, 'isAgeSelected').is_selected():
    x = driver.find_element(By.ID, 'txtAge').text
    print(x)

# Multiple Checkbox
checkboxes = driver.find_elements(By.XPATH, '(//div[@class="panel-body"])[3]/div[@class="checkbox"]')
# for i in checkboxes:
#     print(i.text)
#     Options = ['Option 2', 'Option 4']
#     for j in Options:
#         if i.text == j:
#             i.find_element(By.CSS_SELECTOR, 'input.cb1-element').click()
#             i.find_element(By.CSS_SELECTOR, 'input.cb1-element').is_selected()


def select_options(element_list, value):
    if not value[0] == 'all':
        for i in element_list:
            print(i.text)
            for j in range(len(value)):
                if i.text == value[j]:
                    i.find_element(By.CSS_SELECTOR, 'input.cb1-element').click()
                    i.find_element(By.CSS_SELECTOR, 'input.cb1-element').is_selected()
                    break
    else:
        for i in element_list:
            print(i.text)
            if not i.is_selected():
                i.find_element(By.CSS_SELECTOR, 'input.cb1-element').click()


select_options(checkboxes, ['Option 1', 'Option 4'])
select_options(checkboxes, ['all'])
time.sleep(20)
driver.quit()
