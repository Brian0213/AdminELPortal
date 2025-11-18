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

class Test_Publish_VCBC_to_Faculty(BaseTest):

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying VCBCs Publish to Faculty Test********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        time.sleep(3)
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.vcb.clickVCBCMgt()
        self.vcb.tabRegular()
        # self.logger.info("******** Select the VCBC********")
        # self.vcb.singleVCBC()
        # self.logger.info("******** Click the Publish to Faculty Button********")
        # self.vcb.publishtoFaculty()
        # self.logger.info("******** Click the Publish Success Modal********")
        # self.vcb.vcbcPubSuccess()
        # self.logger.info("******** Close the Browser********")
        # self.elportal.quit()
        # self.logger.info("**********VCBC Publish to Faculty Test is Successful********")








