import time
import os
from selenium import webdriver  # pip install selenium==3.5.0
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from Helpers.Browsers import Browser
from locators.Locator import *



class Web(Browser):


    def is_header_logo_available(self):
        self.driver.find_element_by_css_selector(Results_page_header_logo)