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

class Test_Transfer_Rotation(BaseTest):

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Rotation Start Coordination Test********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        self.logger.info("********Click the Rotation Transfer Button********")
        self.dfc.rotationTransfer()
        self.logger.info("********Switch to the Transfer Rotation Modal********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click the Start Coordination Button********")
        self.dfc.transferRotationSpec()
        self.dfc.btnTransferClose()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Start Coordination Test is Successful********")








