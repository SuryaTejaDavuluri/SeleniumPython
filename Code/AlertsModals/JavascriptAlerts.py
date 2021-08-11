from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options = webdriver.ChromeOptions()
options.headless = False

browser = "chrome"
if browser == "chrome":
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

driver.find_element(By.LINK_TEXT, 'Alerts & Modals').click()
driver.find_element(By.LINK_TEXT, 'Javascript Alerts').click()
print(driver.title)

driver.find_element(By.XPATH, '(//button[contains(@class,"btn")])[1]').click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element(By.XPATH, '(//button[contains(@class,"btn")])[2]').click()
print(alert.text)
alert.accept()

driver.find_element(By.XPATH, '(//button[contains(@class,"btn")])[3]').click()
print(alert.text)
alert.send_keys('Hurraahhhh')
alert.accept()

text = driver.find_element(By.ID, 'prompt-demo')
print(text.text)


driver.quit()
