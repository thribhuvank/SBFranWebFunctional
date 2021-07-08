from selenium.webdriver.common.by import By


class BillingExDashboard:

    def __init__(self, driver):
        self.driver = driver

    dashboard = (By.XPATH, "//a[@href='/sb/dpt/billing/dashboard']")

    def clickOnDashboard(self):
        return self.driver.find_element(*BillingExDashboard.dashboard).click()

