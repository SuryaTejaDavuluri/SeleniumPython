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
driver.find_element(By.LINK_TEXT, 'Bootstrap Alerts').click()
print(driver.title)


def alert_message(alerttype, category):
    buttons = driver.find_elements(By.XPATH, '//button[contains(@class,"' + category + '")]')
    msg = driver.find_elements(By.XPATH, '//div[contains(@class,"' + alerttype.lower() + '")]')
    for i in buttons:
        print(i.text)
        if alerttype in i.text:
            i.click()
    for j in msg:
        if "message" in j.text:
            print(j.text)


alert_message('Normal', 'danger')
# Normal,Auto  success,warning,info,danger

driver.quit()
