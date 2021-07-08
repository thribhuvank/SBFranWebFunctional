from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@id='mobile']")
    password = (By.XPATH, "//input[@name='password']")
    submitButton = (By.XPATH, "//button[@type='submit']")
    navigate = (By.XPATH, "//button[contains(text(),'Lets Navigate')]")
    passworderror = (By.CSS_SELECTOR, "label#validation-password-error")
    usernameerror = (By.CSS_SELECTOR, "label#validation-email-error")
    welcome = (By.CSS_SELECTOR, "h2")
    welcome2 = (By.CSS_SELECTOR, "h3")

    def enterUserName(self):
        return self.driver.find_element(*Login.username)

    def getPasswordErrorMsg(self):
        return self.driver.find_element(*Login.passworderror).text

    def getUsernameErrorMsg(self):
        return self.driver.find_element(*Login.usernameerror).text

    def enterPassword(self):
        return self.driver.find_element(*Login.password)

    def clickOnSubmit(self):
        return self.driver.find_element(*Login.submitButton).click()

    def getWelcomeNote(self):
        return self.driver.find_element(*Login.welcome).text

    def getWelcomeNote2(self):
        return self.driver.find_element(*Login.welcome2).text

    def clickOnNavigate(self):
        return self.driver.find_element(*Login.navigate).click()
