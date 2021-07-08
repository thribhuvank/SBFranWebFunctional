from selenium.webdriver.common.by import By


class UploadGRNIS:

    def __init__(self, driver):
        self.driver = driver

    assigntome = (By.XPATH, "//p[contains(text(),'Assigned to me')]")
    asgtomeinv = (By.XPATH, "//div[contains(@class,'title-div')]")
    asgscroll = "//button[contains(text(),'Unassign')]"
    fileUpload = (By.XPATH, "//input[contains(@class,'files-input')]")
    UploadNow = (By.XPATH, "//button[contains(text(),'Upload Now')]")

    def clickOnAssignToMe(self):
        return self.driver.find_element(*UploadGRNIS.assigntome).click()

    def clickOnAssignToMeInv(self):
        return self.driver.find_elements(*UploadGRNIS.asgtomeinv)

    def uploadFile(self):
        return self.driver.find_element(*UploadGRNIS.fileUpload)

    def clickOnUploadNow(self):
        return self.driver.find_element(*UploadGRNIS.UploadNow).click()

    # assign IS
    selectEx = (By.XPATH, "//select[@name='select']")
    selectExIS = (By.XPATH, "//option[@value='24']")
    assignButton = (By.XPATH, "//button[contains(text(),'Assign')]")

    def clickOnSelectEx(self):
        return self.driver.find_element(*UploadGRNIS.selectEx).click()

    def selectEXGRN(self):
        return self.driver.find_element(*UploadGRNIS.selectExIS).click()

    def assignIS(self):
        return self.driver.find_element(*UploadGRNIS.assignButton).click()

    # validate Invoice number
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*UploadGRNIS.values)

    # Unassign
    unassign = (By.XPATH, "//button[contains(text(),'Unassign')]")
    unassignscrollup = "//button[contains(text(),'Upload Now')]"

    def clickOnUnassign(self):
        return self.driver.find_element(*UploadGRNIS.unassign).click()


