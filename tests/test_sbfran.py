import time

import autoit
import pytest
from selenium.webdriver.common.keys import Keys

from pageObjects.AccDashboard import AccDashboard
from pageObjects.AccFinalVal import AccFinalVal
from pageObjects.AccHold import AccHold
from pageObjects.AccUploadInvoice import AccUpLoadInv
from pageObjects.BillEx import BillEx
from pageObjects.BillingDashboard import BillingDashboard
from pageObjects.FranAck import FranAck
from pageObjects.FranCompletedInvs import FranCompletedInvs
from pageObjects.FranDashboard import FranDashboard
from pageObjects.FranRejectedBySB import FranRejBySB
from pageObjects.GRNISHold import GRNISHold
from pageObjects.GrnIS import GrnIS
from pageObjects.Login import Login
from pageObjects.Logout import Logout
from pageObjects.Redo import Redo
from pageObjects.RejectedBySB import RejectedBySB
from pageObjects.SBFranApproval import SBFranApproval
from pageObjects.UploadGRNIS import UploadGRNIS
from pageObjects.pvc import Pvc
from utilities.BaseClass import BaseClass

InvoiceNumber = "FRANSBDPT1001"
AccInvNumberRej = "SBACCDPTREJ1001"
AccInvNumberAccept = "SBACCDPTACPT1001"


class TestSB(BaseClass):
    # Login validations
    def test_franLoginWithoutPassword(self):
        login = Login(self.driver)
        login.enterUserName().send_keys("9880308886")
        time.sleep(1)
        login.clickOnSubmit()
        print(login.getPasswordErrorMsg())

    def test_franLoginWithoutUsername(self):
        login = Login(self.driver)
        self.driver.refresh()
        time.sleep(1)
        login.enterPassword().send_keys("shop@2021")
        login.clickOnSubmit()
        print(login.getUsernameErrorMsg())

    def test_franLoginWithoutUsernameAndPassword(self):
        login = Login(self.driver)
        self.driver.refresh()
        time.sleep(1)
        login.clickOnSubmit()
        print(login.getUsernameErrorMsg())
        print(login.getPasswordErrorMsg())

    def test_franLoginWithInvalidUsername(self):
        login = Login(self.driver)
        self.driver.refresh()
        login.enterUserName().send_keys("1234567890")
        login.enterPassword().send_keys("shop@2021")
        login.clickOnSubmit()
        self.handlePopupMsg()

    def test_franLoginWithInvalidPassword(self):
        login = Login(self.driver)
        self.driver.refresh()
        login.enterUserName().send_keys("9880308886")
        login.enterPassword().send_keys("abc@2021")
        login.clickOnSubmit()
        self.handlePopupMsg()

    # login with valid username and password
    def test_franLoginWithValidCredentials(self):
        login = Login(self.driver)
        self.driver.refresh()
        login.enterUserName().send_keys("9880308886")
        login.enterPassword().send_keys("shop@2021")
        login.clickOnSubmit()

    # Get details after login
    def test_GetWelcomeNote(self):
        login = Login(self.driver)
        print(login.getWelcomeNote())
        print(login.getWelcomeNote2())
        time.sleep(2)

    def test_userNavLogout(self):
        logout = Logout(self.driver)
        logout.clickOnNavLogout()
        print("User logged out successfully")
        TestSB.test_franLoginWithValidCredentials(self)

    def test_NavigateToHome(self):
        login = Login(self.driver)
        login.clickOnNavigate()
        print("User in Home Screen")
        time.sleep(5)

    def test_userLogout(self):
        logout = Logout(self.driver)
        logout.clickOnLogoutIcon()
        logout.clickOnLogout()
        print("User logged out successfully")

    # Franchisee login To use upcoming steps
    def test_franLoginAgain(self):
        login = Login(self.driver)
        login.enterUserName().send_keys("9880308886")
        login.enterPassword().send_keys("shop@2021")
        login.clickOnSubmit()
        TestSB.test_NavigateToHome(self)

    # Dpt Module
    # Franchisee Dpt - Upload Invoice Document
    def test_franchiseeDptDashboard(self):
        frandash = FranDashboard(self.driver)
        frandash.clickOnDashboard()
        print("User in Franchisee DPT Dashboard")

    def test_franUploadInvWithoutAttachedFile(self):
        franupinv = FranDashboard(self.driver)
        franupinv.clickOnUploadNow()
        self.handlePopupMsg()

    def test_franUploadInvWithAttachedFile(self):
        fileupload = FranDashboard(self.driver)
        fileupload.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(2)
        fileupload.clickOnUploadNow()
        time.sleep(1)
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # Accounts
    def test_accLoginWithValidCredentials(self):
        login = Login(self.driver)
        login.enterUserName().send_keys("9066343126")
        login.enterPassword().send_keys("shop@2021")
        login.clickOnSubmit()
        TestSB.test_GetWelcomeNote(self)
        TestSB.test_NavigateToHome(self)

    def test_acc_dashboard(self):
        log = self.getLogger()
        accdash = AccDashboard(self.driver)
        accdash.clickOnDashboard()
        log.info("Accounts DPT Dashboard")

    def test_acc_pvc_invoice(self):
        log = self.getLogger()
        pvc = Pvc(self.driver)
        pvc.clickOnPVC()
        time.sleep(3)
        pvcInvoices = pvc.getPVCinvs()
        for inv in pvcInvoices:
            inv.click()
            break
        time.sleep(1)

    def test_clear_pvc(self):
        clearpvc = Pvc(self.driver)
        clearpvc.clearPVC()
        time.sleep(1)
        clearpvc.clickOnOkclsPVC()
        time.sleep(1)
        self.handlePopupMsg()

    # Initated By Fran, Rejected By SB - starts
    # Accounts pvc invoice reject for image not clear
    def test_updateInvoiceClearImageAsNo(self):
        clearImage = Pvc(self.driver)
        invImageClear = clearImage.clickOnInvClearImageNo()
        for inv in invImageClear:
            inv.click()
            time.sleep(1)
            clearImage.clickOnInvClearImageNoConOk()
            self.handlePopupMsg()
            break
        TestSB.test_userLogout(self)

    # Franchisee Accept rejected invoice from SB
    def test_franRejectedInvFromSBUploadedByFranGrid(self):
        TestSB.test_franLoginWithValidCredentials(self)
        TestSB.test_GetWelcomeNote(self)
        TestSB.test_NavigateToHome(self)
        TestSB.test_franchiseeDptDashboard(self)
        rejgrid = FranRejBySB(self.driver)
        rejgrid.clickOnRejectedBySB()

    def test_franAcceptRejectedInvFromSBUploadedByFran(self):
        acceptrej = FranRejBySB(self.driver)
        acceptrej.clickOnAcceptOnInv()
        acceptrej.clickOnAcceptOnInvNo()
        Invoices = acceptrej.getRejectedInvs()
        for inv in Invoices:
            inv.click()
            break
        acceptrej.clickOnAcceptInInv()
        acceptrej.clickOnAcceptInInvYes()
        self.handlePopupMsg()

    def test_franRejectedBySBGrid(self):
        TestSB.test_franchiseeDptDashboard(self)
        rejinv = RejectedBySB(self.driver)
        RejectedInvGrid = rejinv.getRejectedGrid()
        self.scrollOnceDownArrow(rejinv.scrollpath)
        RejectedInvGrid[-1].click()
        time.sleep(1)

    def test_franRejectedBySBInv(self):
        viewrejinv = RejectedBySB(self.driver)
        viewrejinv.viewRejectedInv()
        Remarks = viewrejinv.getRemark()
        InvoiceRemarks = []
        for remark in Remarks:
            remark = remark.text
            InvoiceRemarks.append(remark)
        print(InvoiceRemarks)
        # assert 'Rejected because the Invoice image is not clear' in InvoiceRemarks

    # Initated By Fran, Rejected By SB for Image not clear - ends
    # Initated By Fran, Rejected By SB for Invoice not in Flex Retail name - starts
    def test_uploadInvForSBPvcReject(self):
        TestSB.test_franchiseeDptDashboard(self)
        TestSB.test_franUploadInvWithAttachedFile(self)

    def test_updateInvoiceClearImageYes(self):
        TestSB.test_accLoginWithValidCredentials(self)
        TestSB.test_acc_dashboard(self)
        TestSB.test_acc_pvc_invoice(self)
        TestSB.test_clear_pvc(self)
        clearImage = Pvc(self.driver)
        invImageClear = clearImage.clickOnInvClearImage()
        for inv in invImageClear:
            inv.click()
            time.sleep(1)
            self.handlePopupMsg()
            break

    def test_updateInvoiceInFlexNameNo(self):
        invFlex = Pvc(self.driver)
        invFlex.updateInvFlexNo()
        invFlex.updateInvFlexNoConfirmOk()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_franAcceptRejectedInvFromSBUploadedByFranNameNotInFlex(self):
        TestSB.test_franRejectedInvFromSBUploadedByFranGrid(self)
        TestSB.test_franAcceptRejectedInvFromSBUploadedByFran(self)
        TestSB.test_franRejectedBySBGrid(self)
        TestSB.test_franRejectedBySBInv(self)
        TestSB.test_franchiseeDptDashboard(self)
        TestSB.test_franUploadInvWithAttachedFile(self)
        TestSB.test_updateInvoiceClearImageYes(self)

    # Initated By Fran, Rejected By SB for Invoice not in Flex Retail name - ends
    # Initated By Fran, Rejected By SB for distributor Creation - starts
    def test_updateInvoiceNameInFlexYes(self):
        invFlex = Pvc(self.driver)
        time.sleep(1)
        invFlex.updateInvFlexYes()
        time.sleep(1)
        self.handlePopupMsg()

    # Email for distributor creation and hold/unhold
    def test_updateInvoiceDistributorNoAvailale(self):
        selectgst = Pvc(self.driver)
        time.sleep(1)
        selectgst.enterGST().send_keys("aqw123")
        time.sleep(1)
        selectgst.clickOnDistriCreate()
        time.sleep(1)
        selectgst.enterEmailDist()
        time.sleep(1)
        selectgst.addEmailDist()
        time.sleep(1)
        selectgst.sendEmailReq()
        self.handlePopupMsg()
        time.sleep(1)
        selectgst.unholdInv()
        time.sleep(1)
        self.handlePopupMsg()

    def test_updateInvoiceDistributor(self):
        selectgst = Pvc(self.driver)
        time.sleep(1)
        selectgst.enterGST().send_keys("Shr")
        time.sleep(1)
        selectgst.enterGST().send_keys("e")
        time.sleep(1)
        selectgst.enterGST().send_keys("e")
        time.sleep(2)
        selectgst.selectGST()
        time.sleep(1)
        gstscroll = selectgst.scrollgstpath
        time.sleep(1)
        self.scrollOnceDownArrow(gstscroll)
        time.sleep(2)
        selectgst.addGST()
        time.sleep(1)
        self.handlePopupMsg()

    # Initated By Fran, Rejected By SB for distributor Creation - ends
    # Initated By Fran, Rejected By SB for Invalid Invoice number - starts
    def test_updateInvalidInvoiceNumber(self):
        invnumber = Pvc(self.driver)
        invnumber.enterInvNumber().send_keys("1")
        time.sleep(1)
        invnumber.clickOnNextAfterIN()
        invnumber.clickOnInvNumberConfirOk()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_franAcceptRejectedInvFromSBUploadedByFranInvalidInvNumber(self):
        TestSB.test_franRejectedInvFromSBUploadedByFranGrid(self)
        TestSB.test_franAcceptRejectedInvFromSBUploadedByFran(self)
        TestSB.test_franRejectedBySBGrid(self)
        TestSB.test_franchiseeDptDashboard(self)
        TestSB.test_franUploadInvWithAttachedFile(self)
        TestSB.test_updateInvoiceClearImageYes(self)
        TestSB.test_updateInvoiceNameInFlexYes(self)
        TestSB.test_updateInvoiceDistributor(self)

    # Initated By Fran, Rejected By SB for Invalid Invoice number - ends
    def test_updateValidInvNumber(self):
        invnumber = Pvc(self.driver)
        invnumber.enterInvNumber().send_keys(InvoiceNumber)
        time.sleep(1)
        invnumber.clickOnNextAfterIN()
        self.handlePopupMsg()

    def test_updateInvAmt(self):
        invamt = Pvc(self.driver)
        invamt.enterInvAmt()
        time.sleep(1)
        invamt.clickOnNextInvAmt()
        self.handlePopupMsg()

    def test_selectInvDate(self):
        invdate = Pvc(self.driver)
        invdate.clickOnDateIcon()
        time.sleep(1)
        invdate.selectInvDate()
        time.sleep(1)
        invdate.clickDateNext()
        self.handlePopupMsg()

    # Process Pvc Invoice from accounts
    def test_accProcessPVCInv(self):
        processpvc = Pvc(self.driver)
        processscroll = processpvc.scrollgstpath
        self.scrollOnceDownArrow(processscroll)
        processpvc.clickOnProcess()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # Negative validations for Upload invoice from Accounts
    def test_accUploadInvoiceWithOutAttachment(self):
        TestSB.test_accLoginWithValidCredentials(self)
        TestSB.test_acc_dashboard(self)
        fileupload = AccUpLoadInv(self.driver)
        fileupload.clickOnAddInvoiceGrid()
        self.scrollOnceDownArrow(fileupload.scrollpath)
        fileupload.clickOnSubmit()
        errors = fileupload.getErrors()
        for error in errors:
            print(error.text)
            break

    def test_accUploadInvoiceWithAttachment(self):
        fileupload = AccUpLoadInv(self.driver)
        fileupload.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(1)

    def test_accUploadInvoiceDonotSelectFranchisee(self):
        selfran = AccUpLoadInv(self.driver)
        self.scrollDownArrow(2, selfran.scrollpath)
        selfran.clickOnSubmit()
        errors = selfran.getErrors()
        for error in errors:
            print(error.text)
            break

    def test_accUploadInvoiceSelectFranchisee(self):
        selfran = AccUpLoadInv(self.driver)
        selfran.clickOnSelectFranchisee()
        time.sleep(1)
        selfran.selectFranchisee()
        selfran.clickOnSubmit()

    def test_accUploadInvoiceDonotEnterInvNumber(self):
        invnum = AccUpLoadInv(self.driver)
        invnum.enterInvNumber().send_keys("1")
        invnum.clickOnSubmit()

    def test_accUploadInvoiceEnterInvNumber(self):
        invnum = AccUpLoadInv(self.driver)
        invnum.enterInvNumber().send_keys(AccInvNumberRej)
        invnum.clickOnSubmit()

    def test_accUploadInvoiceDonotSelectDate(self):
        invdate = AccUpLoadInv(self.driver)
        invdate.clickOnSubmit()

    def test_accUploadInvoiceSelectDate(self):
        invdate = AccUpLoadInv(self.driver)
        invdate.clickOnDateIcon()
        invdate.selectInvDate()
        invdate.clickOnSubmit()

    def test_accUploadInvoiceDonotSelectDistri(self):
        invdist = AccUpLoadInv(self.driver)
        invdist.clickOnSubmit()

    def test_accUploadInvoiceSelectDistri(self):
        invdist = AccUpLoadInv(self.driver)
        invdist.enterGST().send_keys("Shr")
        time.sleep(1)
        invdist.enterGST().send_keys("e")
        time.sleep(1)
        invdist.enterGST().send_keys("e")
        time.sleep(2)
        invdist.selectGST()
        invdist.clickOnSubmit()

    def test_accUploadInvoiceDonotEnterAmt(self):
        invAmt = AccUpLoadInv(self.driver)
        invAmt.clickOnSubmit()

    def test_accUploadInvoiceEnterAmt(self):
        invAmt = AccUpLoadInv(self.driver)
        invAmt.enterInvAmt()
        time.sleep(2)
        invAmt.clickOnReset()
        time.sleep(3)

    # Add invoice with all valid details from accounts
    def test_accUploadInvWithAllDetails(self):
        addinv = AccUpLoadInv(self.driver)
        addinv.uploadFile().send_keys("G:/API/1.jpg")
        addinv.clickOnSelectFranchisee()
        time.sleep(1)
        addinv.selectFranchisee()
        addinv.enterInvNumber().send_keys(AccInvNumberRej)
        addinv.clickOnDateIcon()
        addinv.selectInvDate()
        addinv.enterGST().send_keys("Shr")
        addinv.enterGST().send_keys("e")
        time.sleep(1)
        addinv.enterGST().send_keys("e")
        time.sleep(2)
        addinv.selectGST()
        addinv.enterInvAmt()
        addinv.clickOnSubmit()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_franIniSBFranApprovalGrid(self):
        TestSB.test_franLoginAgain(self)
        franappr = SBFranApproval(self.driver)
        franappr.clickOnDashboard()
        franappr.clickOnIniSBFran()
        self.scrollDownArrow(2, franappr.scrollpath)
        time.sleep(2)

    # Franchisee Reject Invoice uploaded by Accounts
    def test_franIniSBFranApprovalRejectOnInv(self):
        reject = SBFranApproval(self.driver)
        reject.clickOnRejectOninv()
        reject.enterRemark().send_keys("Invalid invoice amount")
        time.sleep(1)
        reject.clickOnRejectOninvYes()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # Accounts accept rejected invoice from franchisee
    def test_accAcceptSBRejectedByFranGrid(self):
        TestSB.test_accLoginWithValidCredentials(self)
        TestSB.test_acc_dashboard(self)
        rejfran = SBFranApproval(self.driver)
        rejfran.clickOnRejByFran()
        Invoice = rejfran.getInvoices()
        for inv in Invoice:
            inv.click()
            break
        rejfran.clickOnAccept()
        rejfran.clickOnAcceptYes()
        self.handlePopupMsg()

    # Again Accounts upload invoice for franchisee to approve
    def test_accUploadInvforfranApprove(self):
        TestSB.test_acc_dashboard(self)
        approvefran = SBFranApproval(self.driver)
        approvefran.clickOnAddInvoiceGrid()
        addinv = AccUpLoadInv(self.driver)
        addinv.uploadFile().send_keys("G:/API/1.jpg")
        addinv.clickOnSelectFranchisee()
        time.sleep(1)
        addinv.selectFranchisee()
        addinv.enterInvNumber().send_keys(AccInvNumberAccept)
        addinv.clickOnDateIcon()
        addinv.selectInvDate()
        addinv.enterGST().send_keys("Shr")
        addinv.enterGST().send_keys("e")
        time.sleep(1)
        addinv.enterGST().send_keys("e")
        time.sleep(2)
        addinv.selectGST()
        addinv.enterInvAmt()
        addinv.clickOnSubmit()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # Franchisee approved invoice uploaded by accounts
    def test_franIniSBFranApprovalAccept(self):
        TestSB.test_franIniSBFranApprovalGrid(self)
        accept = SBFranApproval(self.driver)
        Invoice = accept.getInvoices()
        for inv in Invoice:
            inv.click()
            break
        accept.clickOnApprove()
        confirmYes = accept.clickOnApproveYes()
        confirmYes[0].click()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # After Approved from franchisee procced fr GRNIS
    def test_accAfterApprovalFromFranProcessInvToGRNIS(self):
        TestSB.test_accLoginWithValidCredentials(self)
        TestSB.test_acc_dashboard(self)
        TestSB.test_acc_pvc_invoice(self)
        processpvc = Pvc(self.driver)
        processpvc.clickOnProcess()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # Franchisee/Accounts Invoice upload and PVC validations ends here
    # Billing GRN/IS starts here
    # Billing Admin login
    def test_billingAdminLoginWithValidCredentials(self):
        login = Login(self.driver)
        login.enterUserName().send_keys("9898989898")
        login.enterPassword().send_keys("Rohit@5678")
        login.clickOnSubmit()
        TestSB.test_GetWelcomeNote(self)
        TestSB.test_NavigateToHome(self)

    def test_billingDPTDashboard(self):
        billdash = BillingDashboard(self.driver)
        billdash.clickOnBillDashboard()
        print("Billing DPT Dashboard")

    def test_billingGetGRNISInvs(self):
        grnis = GrnIS(self.driver)
        grnis.clickOnGRNIS()
        time.sleep(2)
        grnISInvs = grnis.getGRNISInvs()
        for inv in grnISInvs:
            inv.click()
            break
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        self.scrollOnceDownArrow(grnis.grnisscroll)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'

    def test_billDonotSelectExForGRNAssign(self):
        assigngrn = GrnIS(self.driver)
        assigngrn.assignGRN()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billAssignExForGrn(self):
        assigngrn = GrnIS(self.driver)
        assigngrn.clickOnSelectEx()
        time.sleep(1)
        assigngrn.selectEXGRN()
        time.sleep(1)
        assigngrn.assignGRN()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billAdminUploadGRNDocForAnotherUserAssign(self):
        uploadgrn = UploadGRNIS(self.driver)
        self.scrollDownArrow(3, uploadgrn.asgscroll)
        time.sleep(1)
        uploadgrn.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(2)
        uploadgrn.clickOnUploadNow()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billAdminUnAssignGrnUser(self):
        unassign = UploadGRNIS(self.driver)
        self.scrollUpArrow(4, unassign.unassignscrollup)
        unassign.clickOnUnassign()
        self.handlePopupMsg()

    def test_billAdminHoldInvoivce(self):
        grnhold = GRNISHold(self.driver)
        grnhold.clickOnBillDashboard()
        grnhold.clickOnGRNIS()
        time.sleep(2)
        grnISInvs = grnhold.getGRNISInvs()
        for inv in grnISInvs:
            inv.click()
            break
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'

    # GRNIS hold invoice
    def test_billAdminAddInvoiceToHold(self):
        grnhold = GRNISHold(self.driver)
        grnhold.clickOnHold()
        grnhold.clickOnConfirYes()
        self.handlePopupMsg()
        grnhold.enterHoldReason()
        grnhold.clickOnConfirYes()
        self.handlePopupMsg()

    def test_billingAdminViewHoldInvoice(self):
        viewhold = GRNISHold(self.driver)
        viewhold.clickOnBillDashboard()
        viewhold.clickONHoldGrid()
        Invoices = viewhold.getInvoices()
        for inv in Invoices:
            inv.click()
            break
        time.sleep(2)
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'

    # View hold invoice in accounts dashboard
    def test_accViewHoldInvoices(self):
        TestSB.test_userLogout(self)
        TestSB.test_accLoginWithValidCredentials(self)
        TestSB.test_acc_dashboard(self)
        acchold = AccHold(self.driver)
        self.scrollOnceDownArrow(acchold.holdscrolldown)
        acchold.clickOnHoldInvGrid()
        Invoices = acchold.viewHoldInvoices()
        for inv in Invoices:
            inv.click()
            break
        time.sleep(1)

    # print hold invoice details
    def test_accGetHoldInvoiceDetails(self):
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # GRNIS unhold done
    def test_billingAdminUnHoldInvoice(self):
        TestSB.test_billingAdminLoginWithValidCredentials(self)
        TestSB.test_billingAdminViewHoldInvoice(self)
        unhold = GRNISHold(self.driver)
        self.scrollOnceDownArrow(unhold.unholdscroll)
        TestSB.test_billAssignExForGrn(self)
        self.scrollUpArrow(16, unhold.unholdscrollup)
        time.sleep(2)
        unhold.clickOnUnHold()
        time.sleep(1)
        unhold.clickOnConfirYes()
        self.handlePopupMsg()
        unhold.enterUnHoldReason()
        time.sleep(1)
        unhold.clickOnConfirYes()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_billingExLoginWithValidCredentials(self):
        login = Login(self.driver)
        login.enterUserName().send_keys("8105425516")
        login.enterPassword().send_keys("shop@2021")
        login.clickOnSubmit()
        TestSB.test_GetWelcomeNote(self)
        TestSB.test_NavigateToHome(self)

    def test_billingExDPTDashboard(self):
        billdash = BillingDashboard(self.driver)
        billdash.clickOnBillDashboard()
        print("Billing DPT Dashboard")

    def test_billingExNotAssignedToMe(self):
        notassign = BillEx(self.driver)
        notassign.clickOnNOtAssigned()
        Invoices = notassign.getInvoices()
        for inv in Invoices:
            inv.click()
            break
        time.sleep(1)
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'

    def test_billExSelfAssignInvoice(self):
        selfassign = GrnIS(self.driver)
        selfassign.assignGRN()
        self.handlePopupMsg()
        selfassign.clickOnSelectEx()
        time.sleep(1)
        selfassign.selectEXGRN()
        selfassign.assignGRN()
        self.handlePopupMsg()
        time.sleep(15)

    def test_billExUploadWithoutGRNDocument(self):
        uploadgrn = UploadGRNIS(self.driver)
        self.scrollOnceDownArrow(uploadgrn.asgscroll)
        uploadgrn.clickOnUploadNow()
        self.handlePopupMsg()

    def test_billExAssignToMe(self):
        TestSB.test_billingExDPTDashboard(self)
        notassign = BillEx(self.driver)
        notassign.clickOnAssignToMeGrid()
        Invoices = notassign.getInvoices()
        for inv in Invoices:
            inv.click()
            break
        time.sleep(1)
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'

    def test_billExUploadWithGRNDocument(self):
        uploadgrn = UploadGRNIS(self.driver)
        self.scrollOnceDownArrow(uploadgrn.asgscroll)
        uploadgrn.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(2)
        uploadgrn.clickOnUploadNow()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billExAssignEXforIS(self):
        asgIs = UploadGRNIS(self.driver)
        asgIs.assignIS()
        self.handlePopupMsg()
        asgIs.clickOnSelectEx()
        asgIs.selectEXGRN()
        time.sleep(2)
        asgIs.assignIS()
        time.sleep(1)
        self.handlePopupMsg()

    def test_test_billExUploadISDocument(self):
        uploadIS = UploadGRNIS(self.driver)
        self.scrollDownArrow(4, uploadIS.asgscroll)
        uploadIS.clickOnUploadNow()
        self.handlePopupMsg()
        time.sleep(1)
        uploadIS.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(2)
        uploadIS.clickOnUploadNow()
        time.sleep(1)
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    # Billing hold/unhold, Assign grnis and upload grnis documents ends here
    # Accounts Final validation starts here
    def test_accFinalValidationGrid(self):
        TestSB.test_accLoginWithValidCredentials(self)
        TestSB.test_acc_dashboard(self)
        fvinv = AccFinalVal(self.driver)
        fvinv.clickOnFVGrid()
        time.sleep(1)
        Invoices = fvinv.getInvoices()
        for inv in Invoices:
            inv.click()
            break
        time.sleep(1)

    # Accounts Clear Final validation
    def test_accFinalValidationClearFV(self):
        clearfv = AccFinalVal(self.driver)
        clearfv.clearFV()
        clearfv.clickOnOkclsFV()
        time.sleep(2)
        self.handlePopupMsg()

    # Accounts Update Invoice amount not egual to grn amt
    def test_accFVInvAmtNotEqlGrnAmt(self):
        invGRnAmtNo = AccFinalVal(self.driver)
        invGRnAmtNo.clickOnInvAmteqsGrnAmtNo()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Update grn amt not egual to is amt
    def test_accFVGrnAmtNotEglISAmt(self):
        invGRnAmtNo = AccFinalVal(self.driver)
        invGRnAmtNo.clickOnGrnAmtISAmtNo()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Update grn not done for correct store
    def test_accFVInvNotDoneForCurrentStore(self):
        isStoreNo = AccFinalVal(self.driver)
        isStoreNo.isInvStoreNo()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Update free articles not added
    def test_accFVInvNotAddedFreeArticleNo(self):
        freeartNo = AccFinalVal(self.driver)
        freeartNo.freeArticleAddedNo()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Final Validation Rejected
    def test_accFVInvProccedforRedo(self):
        processfs = AccFinalVal(self.driver)
        processfs.clickOnProcess()
        time.sleep(1)
        processfs.clickOnConfirmOk()
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_billAdminRedoGrid(self):
        TestSB.test_billingAdminLoginWithValidCredentials(self)
        TestSB.test_billingDPTDashboard(self)
        redoinv = Redo(self.driver)
        redoinv.clickOnRedo()
        Invoices = redoinv.getInvoices()
        for inv in Invoices:
            inv.click()
            break
        time.sleep(1)
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'

    def test_billAdminSelfAssignRedoInvGRN(self):
        assigngrn = Redo(self.driver)
        assigngrn.clickOnSelectEx()
        time.sleep(1)
        assigngrn.selectEXGRN()
        time.sleep(1)
        assigngrn.assignGRN()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billAdminUploadGRNDocument(self):
        uploadgrn = Redo(self.driver)
        self.scrollDownArrow(5, uploadgrn.asgscroll)
        time.sleep(1)
        uploadgrn.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(2)
        uploadgrn.clickOnUploadNow()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billAdminSelfAssignRedoInvForIS(self):
        assignis = Redo(self.driver)
        assignis.clickOnSelectEx()
        time.sleep(1)
        assignis.selectEXGRN()
        time.sleep(1)
        assignis.assignGRN()
        time.sleep(1)
        self.handlePopupMsg()

    def test_billAdminUploadISDocument(self):
        uploadIS = Redo(self.driver)
        self.scrollDownArrow(3, uploadIS.asgscroll)
        time.sleep(1)
        uploadIS.uploadFile().send_keys("G:/API/1.jpg")
        time.sleep(2)
        uploadIS.clickOnUploadNow()
        time.sleep(1)
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_accDoFinalValidationForRedoInvoice(self):
        TestSB.test_accFinalValidationGrid(self)
        TestSB.test_accFinalValidationClearFV(self)

    # Accounts Update Invoice amount egual to grn amt
    def test_accFVInvAmtEqlGrnAmt(self):
        invGRnAmtYes = AccFinalVal(self.driver)
        invGRnAmtYes.clickOnInvAmteqsGrnAmtYes()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Update grn amt egual to is amt
    def test_accFVGrnAmtEglISAmt(self):
        invGRnAmtYes = AccFinalVal(self.driver)
        invGRnAmtYes.clickOnGrnAmtISAmtYes()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Update grn done for correct store
    def test_accFVInvDoneForCurrentStore(self):
        isStoreYes = AccFinalVal(self.driver)
        isStoreYes.isInvStoreYes()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Update free articles added
    def test_accFVInvNotAddedFreeArticleYes(self):
        freeartYes = AccFinalVal(self.driver)
        freeartYes.freeArticleAddedYes()
        time.sleep(2)
        self.handlePopupMsg()
        time.sleep(1)

    # Accounts Final Validation Done and Send for Fran Ack
    def test_accFVInvProccedforFranAck(self):
        processfs = AccFinalVal(self.driver)
        processfs.clickOnProcess()
        time.sleep(1)
        self.handlePopupMsg()
        TestSB.test_userLogout(self)

    def test_franAckForProcessCompletedInvoice(self):
        TestSB.test_franLoginAgain(self)
        TestSB.test_franchiseeDptDashboard(self)
        franack = FranAck(self.driver)
        franack.clickOnCompletedACk()
        time.sleep(1)

    def test_franApproveForProcessCompletedInvoice(self):
        franack = FranAck(self.driver)
        procInvs = franack.getProComInvs()
        for inv in procInvs:
            inv.click()
            break
        time.sleep(1)
        franack.clickOnApprove()
        time.sleep(1)
        franack.clickOnPopOk()
        self.handlePopupMsg()

    def test_franCompletedInvoices(self):
        TestSB.test_franchiseeDptDashboard(self)
        francompleted = FranCompletedInvs(self.driver)
        scrollpath = francompleted.scrollpath
        self.scrollOnceDownArrow(scrollpath)
        francompleted.clickOnCompltedInv()
        time.sleep(2)
        CompletedInvs = francompleted.viewCompletedInvoice()
        time.sleep(2)
        for inv in CompletedInvs:
            inv.click()
            break
        time.sleep(2)
        InvDetails = self.getInvoiceDetails()
        print(InvDetails)
        time.sleep(1)
        assert AccInvNumberAccept in InvDetails, 'Invoice Number Not Matching'












