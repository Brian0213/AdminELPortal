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

class Test_Edit_Sites(BaseTest):

    site  = "Ronald Reagan UCLA Medical Center"
    # siteaddress = "12 Nicholas Drive North Alpine, AK 99903"
    # extnote = "Find the right care for you"
    # intnote = "Find the right care for you"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Site Edit********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Sites menu********")
        self.dfc.clickSites()
        self.logger.info("******** Search for a Site********")
        self.dfc.fieldSearchSite(self.site)
        # self.elportal.switch_to.window(parentwindowid)
        time.sleep(3)
        self.logger.info("******** Click the Site View Button********")
        self.dfc.btnViewSite()
        self.logger.info("******** Click the Add Task Button on Site's Details Page********")
        self.dfc.btnSiteAddTask()
        self.logger.info("********Switch to the Assign Task to Site Modal********")
        self.logger.info("******** Click the Available Tasks Field********")
        self.dfc.fieldAvailableTasks()
        self.logger.info("******** Select a Task********")
        dropdown_option=self.dfc.taskBringChildtoWork()
        self.logger.info("******** Define Variable for ActionChains********")
        act = ActionChains(self.elportal)
        self.logger.info("******** Select the Task********")
        act.key_down(Keys.CONTROL).click(dropdown_option).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        self.logger.info("******** Click the Type Field********")
        self.dfc.fieldType()
        self.logger.info("******** Select a Type********")
        self.dfc.typePracticum()
        self.logger.info("******** Click the Assign and Close Button********")
        self.dfc.btnAssignandClose()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Edit Site Test is Successful********")

        # READY

