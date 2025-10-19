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

class Test_Allocate_Slots(BaseTest):

    slot = "1"

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Slots Allocation********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.vcb.clickVCBCMgt()
        self.logger.info("******** Select the VCBC********")
        self.vcb.singleVCBC()
        self.logger.info("******** Click Allocate Slots Button ********")
        self.vcb.allocateSlotBtn()
        self.logger.info("********Switch to the Allocate Slots Modal********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click the Select Faculty********")
        self.vcb.selFaculty()
        self.logger.info("******** Select A Faculty********")
        self.vcb.facultyProfFadel()
        self.logger.info("******** Enter Slot Number********")
        self.vcb.allocateSlots(self.slot)
        self.logger.info("******** Click the Allocate Button********")
        self.vcb.allocateButton()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Allocate Slots Test is Successful********")








