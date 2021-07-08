from selenium.webdriver.common.by import By


class BillingDashboard:

    def __init__(self, driver):
        self.driver = driver

    dashboard = (By.XPATH, "//a[@href='/sb/dpt/billing/dashboard']")

    def clickOnBillDashboard(self):
        return self.driver.find_element(*BillingDashboard.dashboard).click()

