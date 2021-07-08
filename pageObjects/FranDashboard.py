from selenium.webdriver.common.by import By


class FranDashboard:

    def __init__(self, driver):
        self.driver = driver

    franDash = (By.XPATH, "//a[@href='/sb/dpt/franchisee/dashboard']")
    fileUploadButton = (By.XPATH, "//div[contains(@class, 'upload-text')]")
    fileUpload = (By.XPATH, "//input[contains(@class,'files-input')]")
    UploadNow = (By.XPATH, "//button[contains(text(),'Upload Now')]")
    alertMsg = (By.XPATH, "//div[contains(@class,'sb-alert')]")

    def clickOnDashboard(self):
        return self.driver.find_element(*FranDashboard.franDash).click()

    def clickOnFileUpload(self):
        return self.driver.find_element(*FranDashboard.fileUploadButton).click()

    def uploadFile(self):
        return self.driver.find_element(*FranDashboard.fileUpload)

    def clickOnUploadNow(self):
        return self.driver.find_element(*FranDashboard.UploadNow).click()

    def getAlertMsg(self):
        return self.driver.find_element(*FranDashboard.alertMsg).text
