from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver.get("https://www.seleniumeasy.com/test/")
print(driver.title)
time.sleep(5)
driver.find_element(By.ID, 'at-cv-lightbox-close').click()

driver.find_element(By.LINK_TEXT, 'Input Forms').click()
driver.find_element(By.LINK_TEXT, 'Radio Buttons Demo').click()

# Radio Button Demo
gender = ['Male', 'Female']
for i in gender:
    driver.find_element(By.XPATH, '(//input[@value="' + i + '"])[1]').click()
    driver.find_element(By.ID, 'buttoncheck').click()
    if driver.find_element(By.XPATH, '(//input[@value="' + i + '"])[1]').is_selected():
        x = driver.find_element(By.CLASS_NAME, 'radiobutton').text
        print(x)

# Group Radio Buttons Demo
sex = ['Male', 'Female']
age = ['0 - 5', '5 - 15', '15 - 50']
for j in sex:
    for k in age:
        driver.find_element(By.XPATH, '(//input[@value="' + j + '"])[2]').click()
        driver.find_element(By.XPATH, '//input[@value="' + k + '"]').click()
        driver.find_element(By.XPATH, '(//button[@type="button"])[3]').click()
        if driver.find_element(By.XPATH, '(//input[@value="' + j + '"])[2]').is_selected():
            y = driver.find_element(By.CLASS_NAME, 'groupradiobutton').text
            print(y)

time.sleep(10)
driver.quit()
