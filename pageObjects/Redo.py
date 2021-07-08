from selenium.webdriver.common.by import By


class Redo:
    def __init__(self, driver):
        self.driver = driver

    redogrid = (By.XPATH, "//p[contains(text(),'Redo')]")
    Invoices = (By.XPATH, "//div[contains(@class,'title-div')]")

    def clickOnRedo(self):
        return self.driver.find_element(*Redo.redogrid).click()

    def getInvoices(self):
        return self.driver.find_elements(*Redo.Invoices)

    # Assign Ex for GRN
    selectEx = (By.XPATH, "//select[@name='select']")
    selectExGRN = (By.XPATH, "//option[@value='16']")
    assignButton = (By.XPATH, "//button[contains(text(),'Assign')]")

    def clickOnSelectEx(self):
        return self.driver.find_element(*Redo.selectEx).click()

    def selectEXGRN(self):
        return self.driver.find_element(*Redo.selectExGRN).click()

    def assignGRN(self):
        return self.driver.find_element(*Redo.assignButton).click()

    # GRN upload
    asgscroll = "//button[contains(text(),'Unassign')]"
    fileUpload = (By.XPATH, "//input[contains(@class,'files-input')]")
    UploadNow = (By.XPATH, "//button[contains(text(),'Upload Now')]")

    def uploadFile(self):
        return self.driver.find_element(*Redo.fileUpload)

    def clickOnUploadNow(self):
        return self.driver.find_element(*Redo.UploadNow).click()

    # assign IS
    selectExdrop = (By.XPATH, "//select[@name='select']")
    selectExIS = (By.XPATH, "//option[@value='16']")
    assignISButton = (By.XPATH, "//button[contains(text(),'Assign')]")

    def clickOnSelectExdrop(self):
        return self.driver.find_element(*Redo.selectExdrop).click()

    def selectEXNameGRN(self):
        return self.driver.find_element(*Redo.selectExIS).click()

    def assignIS(self):
        return self.driver.find_element(*Redo.assignISButton).click()