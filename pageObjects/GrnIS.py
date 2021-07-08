from selenium.webdriver.common.by import By


class GrnIS:

    def __init__(self, driver):
        self.driver = driver

    grnisgrid = (By.XPATH, "//p[contains(text(),'GRN + IS')]")
    grnIsInvs = (By.XPATH, "//div[contains(@class,'title-div')]")
    grnisscroll = "//button[contains(text(),'Hold')]"
    notassignscroll = "//button[contains(text(),'Assign')]"

    def clickOnGRNIS(self):
        return self.driver.find_element(*GrnIS.grnisgrid).click()

    def getGRNISInvs(self):
        return self.driver.find_elements(*GrnIS.grnIsInvs)

    # Assign Ex for GRN
    selectEx = (By.XPATH, "//select[@name='select']")
    selectExGRN = (By.XPATH, "//option[@value='24']")
    assignButton = (By.XPATH, "//button[contains(text(),'Assign')]")

    def clickOnSelectEx(self):
        return self.driver.find_element(*GrnIS.selectEx).click()

    def selectEXGRN(self):
        return self.driver.find_element(*GrnIS.selectExGRN).click()

    def assignGRN(self):
        return self.driver.find_element(*GrnIS.assignButton).click()

    # validate Invoice number
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*GrnIS.values)




