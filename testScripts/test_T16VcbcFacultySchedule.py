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

    faculty= "faculty15@nightingale.test"

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
        self.logger.info("******** Click Impersonate Button ********")
        self.vcb.btnImpersonate()
        self.logger.info("********Switch to the Impersonate A User Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Enter the Faculty Email Address********")
        self.vcb.fieldImpersonateFaculty(self.faculty)
        #self.elportal.find_element(By.XPATH, "//input[@id='email']").send_keys("faculty50@nightingale.test")
        self.logger.info("********Click the Impersonate Button to confirm ********")
        self.vcb.btnConfirmImpersonate()
        #self.elportal.find_element(By.XPATH, "//span[normalize-space()='Impersonate']").click()
        time.sleep(2)
        self.logger.info("********Click the Impersonate Button to confirm ********")
        self.vcb.impersonateMyVCBC()
        #self.elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[3]/a/div/div').click()
        self.logger.info("********Click the VCBC Session Name ********")
        self.vcb.vcbcViewButton()
        #self.elportal.find_element(By.XPATH, '//*[@id="f_vcbc_listing"]/div[1]/pbody/div/table/tbody/tr[1]/td[5]/a').click()
        self.logger.info("********Click the Schedule DateButton ********")
        self.vcb.btnScheduleDate()
        #self.elportal.find_element(By.XPATH, "//select[@x-model='sdate']/option[@value='2025-11-10']").click()
        self.logger.info("********Click the Schedule Time Button ********")
        self.vcb.btnScheduleTime()
        #self.elportal.find_element(By.XPATH, "//select[@x-model='stime']/option[@value='08:00']").click()
        self.logger.info("********Click the Schedule Button ********")
        self.vcb.btnSchedule()
        # self.elportal.find_element(By.XPATH, "//button[normalize-space()='Schedule']").click()
        self.logger.info("********Click the Stop Impersonate Button ********")
        self.vcb.btnStop()
        self.logger.info("******** Close the Browser********")
        # self.elportal.close()
        self.logger.info("**********VCBC Add Faculty Schedule Test is Successful********")














