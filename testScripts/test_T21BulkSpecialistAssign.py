import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.PracticumPage import PracticumPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Bulk_Specialist_Assign(BaseTest):

    hour  = "3"

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)


        self.logger.info("******** Verifying Scheduling Creation Test********")
        self.logger.info("******** Define the Job Driver********")
        self.prac = PracticumPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.prac.clickPracticumTab()
        self.logger.info("******** Click SOFEs menu********")
        # self.prac.btnBulkSpecialistAssign()
        self.logger.info("******** Click Create SOFEs Button********")
        # self.prac.btnDownloadUnassignedLearners()
        self.elportal.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/pbody[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/div[1]/button[1]/span[1]").click()
        time.sleep(3)

        self.prac.fieldFromDate()
        self.prac.pickDate(self.elportal, '22')
        self.prac.fieldToDate()
        self.prac.pickDate(self.elportal, '30')
        # time.sleep(3)
        time.sleep(3)


