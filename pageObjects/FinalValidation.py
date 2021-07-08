from selenium.webdriver.common.by import By


class Finalvalidation:

    def __init__(self, driver):
        self.driver = driver

    fvgrid = (By.XPATH, "//p[contains(text(),'Final Validation after IS')]")
    fvInvs = (By.XPATH, "//div[contains(@class,'title-div')]")

    def clickOnFVGrid(self):
        return self.driver.find_element(*Finalvalidation.fvgrid).click()

    def getFVInvs(self):
        return self.driver.find_elements(*Finalvalidation.fvInvs)

    # clear Invoice
    clearButton = (By.XPATH, "//button[contains(text(),'Clear')]")
    clrpopupOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def clearFV(self):
        return self.driver.find_element(*Finalvalidation.clearButton).click()

    def clickOnOkclsFV(self):
        return self.driver.find_element(*Finalvalidation.clrpopupOk).click()

    # inv amt = grn amt
    invamtisgrn = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnInvAmteqsGrnAmt(self):
        return self.driver.find_elements(*Finalvalidation.invamtisgrn)

    # grn amt = is amt
    grnamtis = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnGrnAmtISAmt(self):
        return self.driver.find_elements(*Finalvalidation.grnamtis)

    # grn amt = is amt
    invstore = (By.XPATH, "//button[contains(text(),'Yes')]")

    def isInvStore(self):
        return self.driver.find_elements(*Finalvalidation.invstore)

    # Free article
    freeart = (By.XPATH, "//button[contains(text(),'Yes')]")

    def freeArticleAdded(self):
        return self.driver.find_element(*Finalvalidation.freeart).click()

    # process pvc
    processbutton = (By.XPATH, "//button[contains(text(),'Process')]")

    def clickOnProcess(self):
        return self.driver.find_element(*Finalvalidation.processbutton).click()

    # validate Invoice number
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*Finalvalidation.values)