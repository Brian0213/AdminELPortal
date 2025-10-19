import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Edit_Rotation_Faculty(BaseTest):

    rotatename = "BLC Module"
    month = "September"
    year = "2025"
    dfchour= "10"
    startminute = "30"
    dfcendhour = "4"

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.elp = LoginPage(self.elportal)

        self.logger.info("******** Verifying Edit Faculty Schedule********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]

        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()

        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()

        self.logger.info("******** Select a Rotation********")
        self.dfc.selectRotation()

        self.logger.info("******** Select a Faculty********")
        self.dfc.editFaculty()

        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)

        self.logger.info("******** Click Add DFC Date Field********")
        self.dfc.addDFCDate()

        self.logger.info("******** Select the DFC Month********")
        self.dfc.dFCMonthNov()

        self.logger.info("******** Select the DFC Year********")
        self.dfc.addDFCYear(self.year)

        self.logger.info("******** Select the DFC Date********")
        self.dfc.pickDate(self.elportal, '13')

        self.logger.info("******** Select the DFC Start Hour********")
        self.dfc.dfcStartHour(self.dfchour)

        self.logger.info("******** Select the DFC End Hour********")
        self.dfc.dfcEndHour(self.dfcendhour)

        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.clickSaveCloseBtn()

        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Edit Faculty Schedule Test is Successful********")




