import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Create_SOFES(BaseTest):


    sofename  = "Montgomery"
    sofestate = "AL"
    sofenotes = "New Entry"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)

        self.logger.info("******** Verifying Scheduling Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickSetupTab()
        self.logger.info("******** Click SOFEs menu********")
        self.dfc.clickSOFE()
        self.logger.info("******** Click Create SOFEs Button********")
        self.dfc.createSOFE()
        self.logger.info("********Switch to the Create SOFEs Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.dfc.sofeName(self.sofename)
        self.dfc.sofeState(self.sofestate)
        self.logger.info("******** Switch to the Notes' Iframe********")
        self.dfc.notesIframe()
        self.logger.info("******** Enter the Notes********")
        self.dfc.sofeNotes(self.sofenotes)
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.sofeSaveClose()
        time.sleep(2)
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Create a SOFEs is Successful********")
