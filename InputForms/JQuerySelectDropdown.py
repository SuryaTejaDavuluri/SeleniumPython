from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

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
driver.find_element(By.LINK_TEXT, 'JQuery Select dropdown').click()


def dropdown_with_search(country):
    driver.find_element(By.CLASS_NAME, 'select2-selection__arrow').click()
    driver.find_element(By.XPATH, '(//input[@type="search"])[2]').send_keys(country)
    driver.find_element(By.XPATH, '(//input[@type="search"])[2]').send_keys(Keys.ENTER)




dropdown_with_search('South Africa')
time.sleep(20)
driver.quit()
