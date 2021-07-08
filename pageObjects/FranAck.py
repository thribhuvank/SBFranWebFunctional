from selenium.webdriver.common.by import By


class FranAck:

    def __init__(self, driver):
        self.driver = driver

    procomack = (By.XPATH, "//p[contains(text(),'Processing Complete. Requires my Acknowledgement')]")
    procomInvs = (By.XPATH, "//div[contains(@class,'title-div')]")
    approve = (By.XPATH, "//button[contains(text(),'Approve')]")
    popupOk = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnCompletedACk(self):
        return self.driver.find_element(*FranAck.procomack).click()

    def getProComInvs(self):
        return self.driver.find_elements(*FranAck.procomInvs)

    def clickOnApprove(self):
        return self.driver.find_element(*FranAck.approve).click()

    def clickOnPopOk(self):
        return self.driver.find_element(*FranAck.popupOk).click()

    # validate Invoice number
    values = (By.XPATH, "//div[@class='col-12']/span")

    def getInvValues(self):
        return self.driver.find_elements(*FranAck.values)
