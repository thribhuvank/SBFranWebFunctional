from selenium.webdriver.common.by import By


class FranRejBySB:
    def __init__(self, driver):
        self.driver = driver

    franrejgrid = (By.XPATH, "//p[contains(text(),'Initiated By Me. Rejected by Shopbox')]")
    acceptOnInv = (By.XPATH, "//button[@class='btn-success']/span")
    acceptOnInvNo = (By.XPATH, "//button[contains(text(),'No')]")
    rejectedInvs = (By.XPATH, "//div[contains(@class, 'title-div')]")
    acceptInInv = (By.XPATH, "//button[contains(text(),'Accept')]")
    acceptInInvYes = (By.XPATH, "//button[contains(text(),'Yes')]")

    def clickOnRejectedBySB(self):
        return self.driver.find_element(*FranRejBySB.franrejgrid).click()

    def clickOnAcceptOnInv(self):
        return self.driver.find_element(*FranRejBySB.acceptOnInv).click()

    def clickOnAcceptOnInvNo(self):
        return self.driver.find_element(*FranRejBySB.acceptOnInvNo).click()

    def getRejectedInvs(self):
        return self.driver.find_elements(*FranRejBySB.rejectedInvs)

    def clickOnAcceptInInv(self):
        return self.driver.find_element(*FranRejBySB.acceptInInv).click()

    def clickOnAcceptInInvYes(self):
        return self.driver.find_element(*FranRejBySB.acceptInInvYes).click()

