import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.VCBCPage import VCBCPage
from testScripts.base_test import BaseTest


class Test_Edit_VCBC_Makeup(BaseTest):

    sessionname  = "Working Session for Community Centers"
    coursepick = "repell"
    description = "Find the right care for you"
    slot = "5"
    year ="2026"
    livehour = "9"
    closehour = "5"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)
        self.logger.info("******** Verifying VCBCs Makeup Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click VCBC Management Menu ********")
        self.vcb.clickVCBCMgt()
        self.logger.info("******** Select a VCBC Session********")
        self.vcb.selectVCBC()
        self.logger.info("******** Click Edit VCBC Button ********")
        self.vcb.btnEditVcbc()
        self.logger.info("********Switch to the Create VCBCs Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click the Course Field********")
        self.vcb.vcbcCourses()
        self.logger.info("******** Lookup Course********")
        self.vcb.pickCourseReg2()
        self.logger.info("******** Click the Save Changes Button********")
        self.vcb.vcbcSaveChanges()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********MakeUp VCBCs Creation Test is Successful********")








