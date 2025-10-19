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

class Test_AddFaculty(BaseTest):

    rotatename = "Medical Outreach Orientation"
    month = "November"
    year = "2025"
    dfchour= "8"
    startminute = "30"
    dfcendhour = "4"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)

        self.logger.info("******** Verifying Scheduling Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        self.logger.info("******** Select a Rotation********")
        self.dfc.selectRotation()
        self.logger.info("******** Click Add Day Button********")
        self.dfc.addDay()
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click Faculty Field********")
        self.dfc.clickFaculty()
        self.logger.info("******** Add a Faculty********")
        faculty=self.dfc.addFaculty()
        # faculty=self.elportal.find_element(By.XPATH, '//*[@id="asel_faculty-opt-12"]')
        self.logger.info("******** Define Variable for ActionChains********")
        act = ActionChains(self.elportal)
        act.click(faculty)
        self.logger.info("********Exit the Dropdown Menu********")
        act.key_down(Keys.ESCAPE)
        self.logger.info("********Confirm the ActionChains Actions********")
        act.perform()
        self.logger.info("******** Click Add DFC Date Field********")
        self.dfc.addDFCDate()
        self.logger.info("******** Select the DFC Month********")
        self.dfc.dFCMonthNov()
        self.logger.info("******** Select the DFC Year********")
        self.dfc.addDFCYear(self.year)
        self.logger.info("******** Select the DFC Date********")
        self.dfc.pickDate(self.elportal, '26')
        self.logger.info("******** Select the DFC Start Hour********")
        self.dfc.dfcStartHour(self.dfchour)
        self.logger.info("******** Select the DFC End Hour********")
        self.dfc.dfcEndHour(self.dfcendhour)
        self.logger.info("******** Select the AM/PM********")
        self.dfc.dfcselPM()
        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.clickSaveCloseBtn()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Add Faculty to Rotation Test is Successful********")




