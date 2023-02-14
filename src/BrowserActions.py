from src.error_handler import ErrorHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

import contextlib
import time


class BrowserActions(ErrorHandler):
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay

    @contextlib.contextmanager
    def webdriver(self):
        if self.driver == "Chrome":
            driver = webdriver.Chrome()
            # print(driver)
            yield driver
            # Close the file
            driver.quit()


    def web_quit_browser(self):
        self.driver.quit()

    def web_open_browser(self, driver, url:str="https://google.com/", delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        driver.get(url)

    def web_fullscreen(self, driver):
        driver.fullscreen_window()
   
    def web_access_url(self, driver, url: str, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)
        driver.get(url)

    def web_find_element(self, driver, xpath:str, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        element = driver.find_element(by=By.XPATH, value=xpath)
        return element

    def web_find_elements(self, driver, xpath, delay=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        element = driver.find_elements(by=By.XPATH, value=xpath)
        return element

    def web_click_element(self, driver, xpath, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        try:
            element = self.web_find_element(driver, xpath)
            element.click()
        except ElementNotInteractableException:
            element = self.web_find_elements(driver, xpath)[1]
            element.click()

    def web_send_keys(self, driver, xpath:str, keys:str, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        try:
            element = self.web_find_element(driver, xpath)
            element.send_keys(keys)
        except ElementNotInteractableException:
            element = self.web_find_elements(driver, xpath)[1]
            element.send_keys(keys)

    def web_go_back(self, driver, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)
        
        driver.back()   
    
    def web_go_forward(self, driver, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        driver.forward()

    def web_refresh(self, driver, delay:int=None):
        if delay is None:
            delay = self.delay
        time.sleep(delay)

        driver.refresh()

    