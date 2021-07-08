from selenium.webdriver.common.by import By


class FranCompletedInvs:

    def __init__(self, driver):
        self.driver = driver

    completedInvs = (By.XPATH, "//p[contains(text(),'Completed & Acknowledged')]")
    scrollpath = "//button[contains(text(),'Upload Now')]"
    invs = (By.XPATH, "//div[contains(@class,'title-div')]")

    def clickOnCompltedInv(self):
        return self.driver.find_element(*FranCompletedInvs.completedInvs).click()

    def viewCompletedInvoice(self):
        return self.driver.find_elements(*FranCompletedInvs.invs)

    # validate Invoice number
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*FranCompletedInvs.values)
