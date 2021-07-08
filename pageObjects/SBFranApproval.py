from selenium.webdriver.common.by import By


class SBFranApproval:
    def __init__(self, driver):
        self.driver = driver

    franDash = (By.XPATH, "//a[@href='/sb/dpt/franchisee/dashboard']")
    inisbfrangrid = (By.XPATH, "//p[contains(text(),'Initiated By Shopbox. Awaiting My Approval')]")
    scrollpath = "//button[contains(text(),'Submit')]"

    def clickOnDashboard(self):
        return self.driver.find_element(*SBFranApproval.franDash).click()

    def clickOnIniSBFran(self):
        return self.driver.find_element(*SBFranApproval.inisbfrangrid).click()

    # Reject
    rejectOninv = (By.XPATH, "//span[contains(text(),'Reject')]")
    rejectInInv = (By.XPATH, "//button[contains(text(),'Reject')]")
    rejectOninvConfirmNo = (By.XPATH, "(//button[@type='button'])[6]")
    rejectOninvConfirmYes = (By.XPATH, "(//button[@type='button'])[7]")

    def clickOnRejectOninv(self):
        return self.driver.find_element(*SBFranApproval.rejectOninv).click()

    def clickOnRejectInInv(self):
        return self.driver.find_element(*SBFranApproval.rejectInInv).click()

    def clickOnRejectOninvNo(self):
        return self.driver.find_element(*SBFranApproval.rejectOninvConfirmNo).click()

    def clickOnRejectOninvYes(self):
        return self.driver.find_element(*SBFranApproval.rejectOninvConfirmYes).click()

    # view invoice
    invoices = (By.XPATH, "//div[contains(@class,'title-div')]")

    def getInvoices(self):
        return self.driver.find_elements(*SBFranApproval.invoices)

    # remark
    remark = (By.XPATH, "//textarea[@placeholder='Enter the remark']")

    def enterRemark(self):
        return self.driver.find_element(*SBFranApproval.remark)

    # Rejected By Franchisee
    rejByfran = (By.XPATH, "//p[contains(text(),'Uploaded by me. Acknowledge Rejection by Franchise')]")

    def clickOnRejByFran(self):
        return self.driver.find_element(*SBFranApproval.rejByfran).click()

    # Accept
    acceptbutton = (By.XPATH, "//button[contains(text(),'Accept')]")
    acceptYes = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnAccept(self):
        return self.driver.find_element(*SBFranApproval.acceptbutton).click()

    def clickOnAcceptYes(self):
        return self.driver.find_element(*SBFranApproval.acceptYes).click()

    # Approve Invoice Uploaded by Shopbox
    addinvoicegrid = (By.XPATH, "//p[contains(text(),'Add Invoice')]")

    def clickOnAddInvoiceGrid(self):
        return self.driver.find_element(*SBFranApproval.addinvoicegrid).click()

    approvebutton = (By.XPATH, "//button[contains(text(),'Approve')]")
    approveYes = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnApprove(self):
        return self.driver.find_element(*SBFranApproval.approvebutton).click()

    def clickOnApproveYes(self):
        return self.driver.find_elements(*SBFranApproval.approveYes)







