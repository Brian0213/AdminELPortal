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

class Test_VCBC_FacultySchedule(BaseTest):

    learner= "learner50@learn.nightingale.test"

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Add Learner by Search********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click User Menu Button ********")
        self.vcb.btnUser()
        # self.elportal.find_element(By.XPATH, "//button[normalize-space()='Auto Admin']").click()
        self.logger.info("******** Click Impersonate Button ********")
        self.vcb.btnImpersonate()
        # self.elportal.find_element(By.XPATH, "//button[normalize-space()='Impersonate']").click()
        self.logger.info("********Switch to the Impersonate A User Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Enter the Faculty Email Address********")
        self.vcb.fieldImpersonateLearner(self.learner)
        self.vcb.btnConfirmImpersonate()
        self.vcb.impersonateMyDFC()
        self.logger.info("********Click the Stop Impersonate Button ********")
        self.vcb.btnStop()














