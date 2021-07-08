from selenium.webdriver.common.by import By


class BillEx:
    def __init__(self, driver):
        self.driver = driver

    notassigntome = (By.XPATH, "//p[contains(text(),'Not Assigned')]")
    invoices = (By.XPATH, "//div[contains(@class,'title-div')]")
    scrolldown = "//button[contains(text(),'Assign')]"
    assigntome = (By.XPATH, "//p[contains(text(),'Assigned to me')]")

    def clickOnNOtAssigned(self):
        return self.driver.find_element(*BillEx.notassigntome).click()

    def getInvoices(self):
        return self.driver.find_elements(*BillEx.invoices)

    def clickOnAssignToMeGrid(self):
        return self.driver.find_element(*BillEx.assigntome).click()