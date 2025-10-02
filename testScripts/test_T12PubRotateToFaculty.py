import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.VCBCPage import VCBCPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Publish_to_Faculty_Rotation(BaseTest):

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)

        self.logger.info("******** Verifying Rotation Publish To Faculty Test********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        time.sleep(3)
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        self.dfc.selectRotation()
        self.logger.info("******** Click the Publish to Faculty Button********")
        self.dfc.publishtoFaculty()
        self.logger.info("******** Click the Publish Success Modal********")
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Publish to Faculty Test is Successful********")








