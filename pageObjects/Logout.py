from selenium.webdriver.common.by import By


class Logout:
    def __init__(self, driver):
        self.driver = driver

    logouticon = (By.XPATH, "//div[contains(@class, 'drp-user')]")
    logout = (By.XPATH, "//span[contains(text(),'Logout')]")
    # Navigate
    navlogout = (By.CSS_SELECTOR, "span.logout")

    def clickOnLogoutIcon(self):
        return self.driver.find_element(*Logout.logouticon).click()

    def clickOnLogout(self):
        return self.driver.find_element(*Logout.logout).click()

    def clickOnNavLogout(self):
        return self.driver.find_element(*Logout.navlogout).click()