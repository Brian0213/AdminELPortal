import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_ImpersonateFaculty(BaseTest):

    emailimpersonate ="faculty24@nightingale.test"

    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.elp = LoginPage(self.elportal)

        self.logger.info("******** Verifying Impersonate a Faculty********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        time.sleep(2)
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.logger.info("********Click the User Menu********")
        self.elp.userMenuNav()
        self.logger.info("********Click the Impersonate Button********")
        self.elp.buttonImpersonate()
        self.logger.info("********Switch to the Impersonate A User Modal********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Enter the Email into the Email of User to impersonate field********")
        self.elp.emailImpersonate(self.emailimpersonate)
        self.logger.info("********Click the Impersonate Button********")
        self.elp.Impersonate()
        self.logger.info("********Click the Stop Button to End Impersonation********")
        self.elp.stopImpersonate()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Impersonate a Faculty is Successful********")




