from selenium.webdriver.common.by import By
from selenium import webdriver
from Config.config import TestData
from Pages.BasePage import BasePage


class SimpleDemoPage(BasePage):

    pop_up = (By.ID, 'at-cv-lightbox-close')
    menu_link = (By.LINK_TEXT, 'Input Forms')
    page_link = (By.LINK_TEXT, 'Simple Form Demo')
    buttons = (By.XPATH, '//button[@type="button" and @class="btn btn-default"]')
    message_field = (By.ID, 'user-message')
    message_button = (By.ID, 'display')

    sum1_field = (By.ID, 'sum1')
    sum2_field = (By.ID, 'sum2')
    value_button = (By.ID, 'displayvalue')



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_page_title(self):
        self.get_title("Selenium Easy")

    def close_pop_up(self):
        self.do_click(self.pop_up)

    def get_menu(self):
        self.do_click(self.menu_link)

    def get_page(self):
        self.do_click(self.page_link)

    def enter_message(self, message):
        self.do_send_keys(self.message_field, message)

    def get_buttons(self):
        buttons_list = self.get_elements_text(self.buttons)
        # print(buttons_list)
        for i in buttons_list:
            # print(i.text)
            if i.text == "Show Message":
                i.click()

    def show_message(self):
        msg = self.get_element_text(self.message_button)
        print(msg.text)
        return msg.text

    def enter_sum1(self, sum1):
        self.do_send_keys(self.sum1_field, sum1)

    def enter_sum2(self, sum2):
        self.do_send_keys(self.sum2_field, sum2)

    def calc_sum(self):
        buttons_list = self.get_elements_text(self.buttons)
        for i in buttons_list:
            # print(i.text)
            if i.text == "Get Total":
                i.click()

    def show_sum_value(self):
        value = self.get_element_text(self.value_button)
        print(value)
        return value.text






