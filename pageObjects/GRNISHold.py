from selenium.webdriver.common.by import By


class GRNISHold:
    def __init__(self, driver):
        self.driver = driver

    # dashboard
    dashboard = (By.XPATH, "//a[@href='/sb/dpt/billing/dashboard']")

    def clickOnBillDashboard(self):
        return self.driver.find_element(*GRNISHold.dashboard).click()

    # GRNIS invoices
    grnisgrid = (By.XPATH, "//p[contains(text(),'GRN + IS')]")
    grnIsInvs = (By.XPATH, "//div[contains(@class,'title-div')]")
    grnisscroll = "//button[contains(text(),'Hold')]"

    def clickOnGRNIS(self):
        return self.driver.find_element(*GRNISHold.grnisgrid).click()

    def getGRNISInvs(self):
        return self.driver.find_elements(*GRNISHold.grnIsInvs)

    # Hold Invoice
    hold = (By.XPATH, "//button[contains(text(),'Hold')]")
    holdreason = (By.XPATH, "//textarea[@placeholder='Enter the reason']")
    confirYes = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnHold(self):
        return self.driver.find_element(*GRNISHold.hold).click()

    def enterHoldReason(self):
        return self.driver.find_element(*GRNISHold.holdreason).send_keys("Payment Not Done")

    def clickOnConfirYes(self):
        return self.driver.find_element(*GRNISHold.confirYes).click()

    # View hold Invoices
    holdgrid = (By.XPATH, "//p[contains(text(),'Hold')]")
    invoices = (By.XPATH, "//div[contains(@class,'title-div')]")
    unholdscroll = "//button[contains(text(),'Unhold')]"
    unholdscrollup = "//button[contains(text(),'Assign')]"
    unhold = (By.XPATH, "//button[contains(text(),'Unhold')]")

    def clickONHoldGrid(self):
        return self.driver.find_element(*GRNISHold.holdgrid).click()

    def getInvoices(self):
        return self.driver.find_elements(*GRNISHold.invoices)

    def clickOnUnHold(self):
        return self.driver.find_element(*GRNISHold.unhold).click()

    def enterUnHoldReason(self):
        return self.driver.find_element(*GRNISHold.holdreason).send_keys("Payment Done Successfully")

    # Get Invoice values
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*GRNISHold.values)


