from selenium.webdriver.common.by import By


class AccFinalVal:
    def __init__(self, driver):
        self.driver = driver

    fvgrid = (By.XPATH, "//p[contains(text(),'Final Validation after IS')]")
    Invoices = (By.XPATH, "//div[contains(@class,'title-div')]")

    def clickOnFVGrid(self):
        return self.driver.find_element(*AccFinalVal.fvgrid).click()

    def getInvoices(self):
        return self.driver.find_elements(*AccFinalVal.Invoices)

    # clear invoice
    clearButton = (By.XPATH, "//button[contains(text(),'Clear')]")
    clrpopupOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def clearFV(self):
        return self.driver.find_element(*AccFinalVal.clearButton).click()

    def clickOnOkclsFV(self):
        return self.driver.find_element(*AccFinalVal.clrpopupOk).click()

    # inv amt = grn amt
    invamtisgrnYes = (By.XPATH, "(//button[@id='invoice_grn_amt'])[1]")
    invamtisgrnNo = (By.XPATH, "(//button[@id='invoice_grn_amt'])[2]")

    def clickOnInvAmteqsGrnAmtYes(self):
        return self.driver.find_element(*AccFinalVal.invamtisgrnYes).click()

    def clickOnInvAmteqsGrnAmtNo(self):
        return self.driver.find_element(*AccFinalVal.invamtisgrnNo).click()

    # grn amt = is amt
    grnamtisYes = (By.XPATH, "(//button[@id='grn_is_amt'])[1]")
    grnamtisNo = (By.XPATH, "(//button[@id='grn_is_amt'])[2]")

    def clickOnGrnAmtISAmtYes(self):
        return self.driver.find_element(*AccFinalVal.grnamtisYes).click()

    def clickOnGrnAmtISAmtNo(self):
        return self.driver.find_element(*AccFinalVal.grnamtisNo).click()

    # grn amt = is amt
    invstoreYes = (By.XPATH, "(//button[@id='is_store'])[1]")
    invstoreNo = (By.XPATH, "(//button[@id='is_store'])[2]")

    def isInvStoreYes(self):
        return self.driver.find_element(*AccFinalVal.invstoreYes).click()

    def isInvStoreNo(self):
        return self.driver.find_element(*AccFinalVal.invstoreNo).click()

    # Free article
    freeartYes = (By.XPATH, "(//button[@id='free_articles'])[1]")
    freeartNo = (By.XPATH, "(//button[@id='free_articles'])[2]")

    def freeArticleAddedYes(self):
        return self.driver.find_element(*AccFinalVal.freeartYes).click()

    def freeArticleAddedNo(self):
        return self.driver.find_element(*AccFinalVal.freeartNo).click()

    # process pvc
    processbutton = (By.XPATH, "//button[contains(text(),'Process')]")
    confirOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def clickOnProcess(self):
        return self.driver.find_element(*AccFinalVal.processbutton).click()

    def clickOnConfirmOk(self):
        return self.driver.find_element(*AccFinalVal.confirOk).click()

