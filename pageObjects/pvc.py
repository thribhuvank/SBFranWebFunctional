from selenium.webdriver.common.by import By


class Pvc:
    def __init__(self, driver):
        self.driver = driver

    pvcGrid = (By.XPATH, "//p[contains(text(),'Preliminary Validation & Categorisation')]")
    pvcInvs = (By.XPATH, "//a[contains(@href,'/sb/dpt/accounts/pvc-edit?invoice_id=')]")

    def clickOnPVC(self):
        return self.driver.find_element(*Pvc.pvcGrid).click()

    def getPVCinvs(self):
        return self.driver.find_elements(*Pvc.pvcInvs)

    # clear pvc
    clearButton = (By.XPATH, "//button[contains(text(),'Clear')]")
    clrpopupOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def clearPVC(self):
        return self.driver.find_element(*Pvc.clearButton).click()

    def clickOnOkclsPVC(self):
        return self.driver.find_element(*Pvc.clrpopupOk).click()

    # invImageClear
    invImageClear = (By.XPATH, "//button[contains(text(),'Yes')]")
    invImageClearNo = (By.XPATH, "//button[contains(text(),'No')]")
    invImageClearNoConfirmOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def clickOnInvClearImage(self):
        return self.driver.find_elements(*Pvc.invImageClear)

    def clickOnInvClearImageNo(self):
        return self.driver.find_elements(*Pvc.invImageClearNo)

    def clickOnInvClearImageNoConOk(self):
        return self.driver.find_element(*Pvc.invImageClearNoConfirmOk).click()

    # invFlex
    invflexYes = (By.XPATH, "//button[contains(text(),'Yes')]")
    invflexNo = (By.XPATH, "//button[contains(text(),'No')]")
    invflexNoConfirOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def updateInvFlexYes(self):
        return self.driver.find_element(*Pvc.invflexYes).click()

    def updateInvFlexNo(self):
        return self.driver.find_element(*Pvc.invflexNo).click()

    def updateInvFlexNoConfirmOk(self):
        return self.driver.find_element(*Pvc.invflexNoConfirOk).click()

    # update gst
    inputgst = (By.XPATH, "//input[@placeholder='Select Gst']")
    selectgst = (By.XPATH, "//ng2-menu-item/div/span")
    scrollgstpath = "//button[contains(text(),'Clear')]"
    addgst = (By.XPATH, "//div[contains(@class,'gst-inputs')]/button")
    distriCreate = (By.XPATH, "//a[contains(text(),'There is no distributor with this GST, Click here ')]")
    distemail = (By.XPATH, "//input[@name='email']")
    addemail = (By.XPATH, "//button[contains(text(),'Add')]")
    sendemailreq = (By.XPATH, "//button[contains(text(),'Send Email Request')]")
    unhold = (By.XPATH, "//button[contains(text(),'Unhold')]")

    def enterGST(self):
        return self.driver.find_element(*Pvc.inputgst)

    def selectGST(self):
        return self.driver.find_element(*Pvc.selectgst).click()

    def addGST(self):
        return self.driver.find_element(*Pvc.addgst).click()

    def clickOnDistriCreate(self):
        return self.driver.find_element(*Pvc.distriCreate).click()

    def enterEmailDist(self):
        return self.driver.find_element(*Pvc.distemail).send_keys("thribhuvan.nxtk@gmail.com")

    def addEmailDist(self):
        return self.driver.find_element(*Pvc.addemail).click()

    def sendEmailReq(self):
        return self.driver.find_element(*Pvc.sendemailreq).click()

    def unholdInv(self):
        return self.driver.find_element(*Pvc.unhold).click()

    # invoice number
    inputInvNum = (By.XPATH, "//input[@name='invoice_number']")
    invNumberNext = (By.XPATH, "//input[@name='invoice_number']/following-sibling::button")
    invNumberconfirOk = (By.XPATH, "//button[contains(text(),'OK')]")

    def enterInvNumber(self):
        return self.driver.find_element(*Pvc.inputInvNum)

    def clickOnNextAfterIN(self):
        return self.driver.find_element(*Pvc.invNumberNext).click()

    def clickOnInvNumberConfirOk(self):
        return self.driver.find_element(*Pvc.invNumberconfirOk).click()

    # invoice amount
    inputinvamt = (By.XPATH, "//input[@name='invoice_amount']")
    invamtnext = (By.XPATH, "//input[@name='invoice_amount']/following-sibling::button")

    def enterInvAmt(self):
        return self.driver.find_element(*Pvc.inputinvamt).send_keys("1000")

    def clickOnNextInvAmt(self):
        return self.driver.find_element(*Pvc.invamtnext).click()

    # inv date
    dateicon = (By.XPATH, "//i[contains(@class, 'fa-calendar')]/parent::span")
    selectdate = (By.XPATH, "//div[contains(text(),'23')]")
    datenextbutton = (By.XPATH, "//label[contains(text(),'Invoice date')]/following-sibling::button")

    def clickOnDateIcon(self):
        return self.driver.find_element(*Pvc.dateicon).click()

    def selectInvDate(self):
        return self.driver.find_element(*Pvc.selectdate).click()

    def clickDateNext(self):
        return self.driver.find_element(*Pvc.datenextbutton).click()

    # process pvc
    processbutton = (By.XPATH, "//button[contains(text(),'Process')]")

    def clickOnProcess(self):
        return self.driver.find_element(*Pvc.processbutton).click()

