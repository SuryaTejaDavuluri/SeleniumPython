from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = False

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
# time.sleep(5)
driver.find_element(By.ID, 'at-cv-lightbox-close').click()

driver.find_element(By.LINK_TEXT, 'Input Forms').click()
driver.find_element(By.LINK_TEXT, 'JQuery Select dropdown').click()


def dropdown_with_search(country):
    driver.find_element(By.CLASS_NAME, 'select2-selection__arrow').click()
    driver.find_element(By.XPATH, '(//input[@type="search"])[2]').send_keys(country)
    driver.find_element(By.XPATH, '(//input[@type="search"])[2]').send_keys(Keys.ENTER)


def dropdown_with_multi(states):
    for state in range(len(states)):
        driver.find_element(By.XPATH, '//input[@type="search"]').send_keys(states[state])
        driver.find_element(By.XPATH, '//input[@type="search"]').send_keys(Keys.ENTER)


def dropdown_with_disabled(territory):
    driver.find_element(By.XPATH, '(//span[@class="select2-selection__arrow"])[2]').click()
    driver.find_element(By.XPATH, '(//input[@type="search"])[2]').send_keys(territory)
    driver.find_element(By.XPATH, '(//input[@type="search"])[2]').send_keys(Keys.ENTER)


category_options = driver.find_elements(By.XPATH, '//select[@id="files"]/optgroup/option')


def dropdown_with_category(value):
    for i in category_options:
        print(i.text)
        if i.text == value:
            i.click()


dropdown_with_search('South Africa')
dropdown_with_multi(['Connecticut', 'Kentucky'])
dropdown_with_disabled('Puerto Rico')
dropdown_with_category('Ruby')

time.sleep(20)
driver.quit()
