import inspect
import time

import pytest
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fileHandler) # file handler object
        logger.addHandler(ch)
        logger.setLevel(logging.DEBUG)
        return logger

    def performSlider(self, slider):
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(40, 0).release().perform()

    def verifyXpathPresence(self, xpathlocator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpathlocator)))
        wait.until(EC.element_to_be_clickable((By.XPATH, xpathlocator)))

    def scrollDown(self, scroll_time,  scrollXpath):
        # scroll_time = 2
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_DOWN)

    def scrollDownArrow(self, scroll_time, scrollXpath):
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.ARROW_DOWN)

    def scrollUpArrow(self, scroll_time, scrollXpath):
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.ARROW_UP)

    def scrollOnceDownArrow(self, scrollXpath):
        scroll_time = 1
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    def scrollOnceUpArrow(self, scrollXpath):
        scroll_time = 1
        scroll = self.driver.find_element_by_xpath(scrollXpath)
        for num in range(0, scroll_time):
            scroll.send_keys(Keys.PAGE_UP)
        time.sleep(1)

    def getfranUserName(self):
        return "9880308886"

    def handlePopupMsg(self):
        log = self.getLogger()
        log.info(self.driver.find_element_by_xpath("//div[contains(@class,'sb-alert')]").text)
        print(self.driver.find_element_by_xpath("//div[contains(@class,'sb-alert')]").text)
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[contains(@class,'sb-alert')]/button").click()

    def getInvoiceDetails(self):
        InvDetails = []
        invValues = self.driver.find_elements_by_xpath("//div[@class='col-12']/span")
        time.sleep(1)
        for value in invValues:
            value = value.text
            time.sleep(1)
            InvDetails.append(value)
        time.sleep(2)
        return InvDetails


