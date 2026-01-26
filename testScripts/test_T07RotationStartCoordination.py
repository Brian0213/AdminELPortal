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

class Test_Start_Coordination_Rotation(BaseTest):

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Rotation Start Coordination Test********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        self.lpg= LoginPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Select DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Select Scheduling menu********")
        self.dfc.clickScheduling()
        # time.sleep(3)
        # self.lpg.semesterNav()
        # self.lpg.semesSpring26()
        self.logger.info("******** Select the DFC Rotation********")
        self.dfc.selectRotation()
        self.logger.info("******** Select the Start Coordination Button********")
        self.dfc.startCoordination()
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Select the Start Coordination Continue Button********")
        self.dfc.continueStartCoordination()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Start Coordination Test is Successful********")








