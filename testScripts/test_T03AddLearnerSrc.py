import time
import sys
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Login_ElPortal(BaseTest):

    learner = "Lelia"

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Add Learner by Search********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        self.dfc.selectRotation()
        self.dfc.addLearner()
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click Learner Field's Dropdown********")
        self.dfc.learnerField()
        self.logger.info("******** Look up a learner's criteria********")
        self.dfc.learnerFieldFD(self.learner)
        self.logger.info("******** Define a Variable for the Learner********")
        dropdown_option = self.dfc.learnSRC()
        self.logger.info("******** Define Variable for ActionChains********")
        act = ActionChains(self.elportal)
        self.logger.info("******** Select the Learner********")
        act.key_down(Keys.CONTROL).click(dropdown_option).key_up(Keys.CONTROL).perform()
        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.clickSaveCloseBtn()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Add Learner by Search Test is Successful********")









        # act.move_to_element(dropdown_option).click().perform()


