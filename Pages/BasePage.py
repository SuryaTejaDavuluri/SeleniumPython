from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import xlrd

from Config.config import TestData

"""This page is parent of all pages"""
"""Contains Generic methods and utilities"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element

    def get_elements_text(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(by_locator))
        return elements

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_contains(title))
        return self.driver.title

    def is_selected(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.element_located_to_be_selected(by_locator))
        return bool(element)
