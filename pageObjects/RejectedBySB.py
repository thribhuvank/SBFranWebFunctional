from selenium.webdriver.common.by import By


class RejectedBySB:
    def __init__(self, driver):
        self.driver = driver

    rejectedgrid = (By.XPATH, "//p[contains(text(), 'Rejected by Shopbox')]")
    scrollpath = "//button[contains(text(),'Upload Now')]"
    scrollpathRe = "//div[contains(@class, 'images-inner-div')]"
    viewinv = (By.XPATH, "//div[contains(@class, 'title-div')]")
    remark = (By.XPATH, "//div[contains(@class, 'label-value')]")

    def getRejectedGrid(self):
        return self.driver.find_elements(*RejectedBySB.rejectedgrid)

    def viewRejectedInv(self):
        return self.driver.find_element(*RejectedBySB.viewinv).click()

    def getRemark(self):
        return self.driver.find_elements(*RejectedBySB.remark)

