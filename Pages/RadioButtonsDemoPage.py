from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class RadioButtonPage(BasePage):

    pop_up = (By.ID, 'at-cv-lightbox-close')
    menu_link = (By.LINK_TEXT, 'Input Forms')
    page_link = (By.LINK_TEXT, 'Radio Buttons Demo')
    gender_select = (By.ID, 'buttoncheck')
    chosen_gender = (By.CLASS_NAME, 'radiobutton')
    # page_link = (By.XPATH, '(//input[@value="' + sex[j] + '"])[2]')
    # buttons = (By.XPATH, '//input[@value="' + age[k] + '"]')
    # message_field = (By.XPATH, '(//button[@type="button"])[3]')
    # message_button = (By.CLASS_NAME, 'groupradiobutton')

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

    # def choose_gender(self, gender):
    #     for i in range(len(gender)):
    #         self.do_click((By.XPATH, '(//input[@value="' + gender[i] + '"])[1]'))
    #         self.do_click(self.gender_select)
    #         if self.is_selected((By.XPATH, '(//input[@value="' + gender[i] + '"])[1]')):
    #             x = self.get_element_text(self.chosen_gender)
    #             return x.text

    def choose_gender(self, gender):
        print(gender)
        # self.do_click((By.XPATH, '(//input[@value="' + gender + '"])[1]'))
        # self.do_click(self.gender_select)
        # if self.is_selected((By.XPATH, '(//input[@value="' + gender + '"])[1]')):
        #     x = self.get_element_text(self.chosen_gender)
        #     return x.text
