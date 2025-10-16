import time
import sys
from weakref import finalize

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.VCBCPage import VCBCPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_VCBC_AddLearnerBySearch(BaseTest):

    email = "learner254@learn.nightingale.test"

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Add Learner by Search********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click VCBC Management Menu ********")
        self.vcb.clickVCBCMgt()
        self.logger.info("******** Select the VCBC Session********")
        self.vcb.singleVCBC()
        self.logger.info("******** Click the Faculty Slot One********")
        self.vcb.btnVcbcSlot1()
        self.logger.info("******** Click the Add Learner Button********")
        self.vcb.btnAddLearner()
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click Learner Field's Dropdown********")
        self.vcb.fieldLearnerEmail(self.email)
        self.logger.info("******** Click the Add Learner Button********")
        self.vcb.btnFormAddLearner()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********VCBC Add Learner Test is Successful********")















