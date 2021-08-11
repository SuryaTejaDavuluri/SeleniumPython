from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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

wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/")
print(driver.title)
popup = wait.until(ec.visibility_of_element_located((By.ID, 'at-cv-lightbox-close')))
popup.click()

driver.find_element(By.LINK_TEXT, 'Alerts & Modals').click()
driver.find_element(By.LINK_TEXT, 'Bootstrap Modals').click()
print(driver.title)


def launch_modal(modal):
    modal_ele = driver.find_elements(By.XPATH, '//*[contains(text(),"' + modal + '")]/parent::div//div//a')
    for i in modal_ele:
        print(i.text)
        if i.text == "Launch modal":
            i.click()


def select_button(modal, button, within):
    buttons = driver.find_elements(By.XPATH, '//*[contains(text(),"' + modal + '")]/parent::div//div[@class="modal-footer"]/a')
    for j in buttons:
        print(j.text)
        if modal == "Multi":
            if within == "again":
                y = wait.until(ec.visibility_of_element_located((By.XPATH, '(//a[@data-toggle="modal"])[3]')))
                y.click()
                wait.until(ec.presence_of_element_located((By.XPATH, '(//*[contains(text(),"Multi")]/parent::div//div[@class="modal-footer"]/a)[4]')))
                inside = driver.find_elements(By.XPATH, '(//*[contains(text(),"Multi")]/parent::div//div[@class="modal-footer"]/a)[4]')
                for k in inside:
                    if "Save" in k.text:
                        time.sleep(3)
                        k.click()
                        break
            elif within == "enough":
                if button in j.text:
                    j.click()
                    break
        elif modal == "Single":
            if button in j.text:
                j.click()
                break


launch_modal('Multi')
select_button('Multi', 'Save', 'again')
# single,Multi
driver.quit()
