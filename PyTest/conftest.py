from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

browser = "chrome"


@pytest.fixture(params=[browser], scope="class")
def init_driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = False
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif request.param == 'edge':
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = web_driver

    print("-----------------Setup-----------------")
    wait = WebDriverWait(web_driver, 20)
    web_driver.maximize_window()
    web_driver.get("https://www.seleniumeasy.com/test/")
    print(web_driver.title)
    popup = wait.until(ec.visibility_of_element_located((By.ID, 'at-cv-lightbox-close')))
    popup.click()

    yield
    print("-----------------teardown-----------------")
    web_driver.quit()
