from selenium.webdriver.common.by import By


class AccUpLoadInv:
    def __init__(self, driver):
        self.driver = driver

    addinvoicegrid = (By.XPATH, "//p[contains(text(),'Add Invoice')]")
    accDash = (By.XPATH, "//a[@href='/sb/dpt/accounts/dashboard']")
    fileUpload = (By.XPATH, "//input[contains(@class,'files-input')]")
    selectfran = (By.XPATH, "//select[@name='fran_id']")
    selfranName = (By.XPATH, "//option[contains(text(),'Hybrid Retails')]")
    inputinvnum = (By.XPATH, "//input[@name='inv_number']")
    scrollpath = "//input[@name='inv_amt']"

    def clickOnDashboard(self):
        return self.driver.find_element(*AccUpLoadInv.accDash).click()

    def clickOnAddInvoiceGrid(self):
        return self.driver.find_element(*AccUpLoadInv.addinvoicegrid).click()

    def uploadFile(self):
        return self.driver.find_element(*AccUpLoadInv.fileUpload)

    def clickOnSelectFranchisee(self):
        return self.driver.find_element(*AccUpLoadInv.selectfran).click()

    def selectFranchisee(self):
        return self.driver.find_element(*AccUpLoadInv.selfranName).click()

    def enterInvNumber(self):
        return self.driver.find_element(*AccUpLoadInv.inputinvnum)

    # inv date
    dateicon = (By.XPATH, "//i[contains(@class, 'fa-calendar')]/parent::span")
    selectdate = (By.XPATH, "//div[contains(text(),'12')]")

    def clickOnDateIcon(self):
        return self.driver.find_element(*AccUpLoadInv.dateicon).click()

    def selectInvDate(self):
        return self.driver.find_element(*AccUpLoadInv.selectdate).click()

    # Gst
    inputgst = (By.XPATH, "//input[@placeholder='Select Gst']")
    selectgst = (By.XPATH, "//ng2-menu-item/div/span")

    def enterGST(self):
        return self.driver.find_element(*AccUpLoadInv.inputgst)

    def selectGST(self):
        return self.driver.find_element(*AccUpLoadInv.selectgst).click()

    # inv amt
    inputinvamt = (By.XPATH, "//input[@name='inv_amt']")
    submitbutton = (By.XPATH, "//button[contains(text(),'Submit')]")
    resetButton = (By.XPATH, "//button[contains(text(),'Reset')]")

    def enterInvAmt(self):
        return self.driver.find_element(*AccUpLoadInv.inputinvamt).send_keys("1000")

    def clickOnSubmit(self):
        return self.driver.find_element(*AccUpLoadInv.submitbutton).click()

    def clickOnReset(self):
        return self.driver.find_element(*AccUpLoadInv.resetButton).click()

    # label error
    labelerror = (By.XPATH, "//label[contains(@class, 'error')]")

    def getErrors(self):
        return self.driver.find_elements(*AccUpLoadInv.labelerror)

