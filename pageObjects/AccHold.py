from selenium.webdriver.common.by import By


class AccHold:
    def __init__(self, driver):
        self.driver = driver

    holdgrid = (By.XPATH, "//p[contains(text(),'Grn Hold Invoices')]")
    invs = (By.XPATH, "//div[contains(@class,'title-div')]")
    holdscrolldown = "//button[contains(@class, 'sb-refresh-btns')]"

    def clickOnHoldInvGrid(self):
        return self.driver.find_element(*AccHold.holdgrid).click()

    def viewHoldInvoices(self):
        return self.driver.find_elements(*AccHold.invs)

    # validate Invoice number
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*AccHold.values)