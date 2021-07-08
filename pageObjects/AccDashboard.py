from selenium.webdriver.common.by import By


class AccDashboard:

    def __init__(self, driver):
        self.driver = driver

    dashboard = (By.XPATH, "//a[@href='/sb/dpt/accounts/dashboard']")

    def clickOnDashboard(self):
        return self.driver.find_element(*AccDashboard.dashboard).click()

