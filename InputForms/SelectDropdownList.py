from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
driver.find_element(By.LINK_TEXT, 'Select Dropdown List').click()

#                       Select List Demo

# Select(driver.find_element(By.ID, 'select-demo')).select_by_visible_text('Tuesday')
# Select(driver.find_element(By.ID, 'select-demo')).select_by_index(5)
# Select(driver.find_element(By.ID, 'select-demo')).select_by_value('Sunday')
# select = Select(single_dropdown_list)


single_dropdown_list = driver.find_element(By.ID, 'select-demo')
week_days = driver.find_elements(By.XPATH, '//select[@id="select-demo"]/option')
day_chosen = driver.find_element(By.CLASS_NAME, 'selected-value')


def select_single_dropdown(element, value, result):
    select = Select(element)
    print(select.is_multiple)
    select.select_by_value(value)
    print(result.text)


def select_options_dropdown(element, value, result):
    select_options = Select(element)
    days_list = select_options.options
    for i in days_list:
        print(i.text)
        if i.text == value:
            i.click()
            break
    print(result.text)


def dropdown_without_select(element, value, result):
    for x in element:
        print(x.text)
        if x.text == value:
            x.click()
            break
    print(result.text)


select_single_dropdown(single_dropdown_list, 'Friday', day_chosen)
select_options_dropdown(single_dropdown_list, 'Tuesday', day_chosen)
dropdown_without_select(week_days, 'Thursday', day_chosen)

#                       Multi Select List Demo

multi_select_states = driver.find_element(By.NAME, 'States')
states_list = driver.find_elements(By.XPATH, '//select[@id="multi-select"]/option')
states_chosen = driver.find_element(By.CLASS_NAME, 'getall-selected')


def multiselect_with_select(element, value, result):
    select = Select(element)
    print(select.is_multiple)
    for i in range(len(value)):
        ActionChains(driver).key_down(Keys.CONTROL).perform()
        select.select_by_value(value[i])
        ActionChains(driver).key_up(Keys.CONTROL).perform()
        driver.find_element(By.ID, 'printAll').click()
    print(result.text)


def multiselect_with_selectoptions(element, value, result):
    select_options = Select(element)
    days_list = select_options.options
    for i in days_list:
        print(i.text)
        for j in range(len(value)):
            select_options.select_by_value(value[j])
            if i.text == value[j]:
                ActionChains(driver).key_down(Keys.CONTROL).click(i).key_up(Keys.CONTROL).perform()
            driver.find_element(By.ID, 'printAll').click()
    print(result.text)


def multiselect_without_select(element, value, result):
    for x in element:
        print(x.text)
        for y in range(len(value)):
            if x.text == value[y]:
                ActionChains(driver).key_down(Keys.CONTROL).click(x).key_up(Keys.CONTROL).perform()
                break
            driver.find_element(By.ID, 'printAll').click()
    print(result.text)


multiselect_with_select(multi_select_states, ['Florida', 'Ohio'], states_chosen)
multiselect_with_selectoptions(multi_select_states, ['California', 'New York'], states_chosen)
multiselect_without_select(states_list, ['New Jersey', 'Pennsylvania'], states_chosen)

time.sleep(20)
driver.quit()
