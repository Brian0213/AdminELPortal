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

class Test_AddLearner_Select(BaseTest):

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Add Learner by Selection********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        self.logger.info("******** Click Rotation********")
        self.dfc.selectRotation()
        self.logger.info("******** Click Add Learner Button********")
        self.dfc.addLearner()
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("******** Click Learner Field's Dropdown********")
        self.dfc.learnerField()
        self.logger.info("******** Define Variable for Learner One********")
        # learnerone = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-7-opt-6"]').click()
        learnerone=self.dfc.learnSLT1()
        # one = self.dfc.learnSLT1()
        time.sleep(2)
        act = ActionChains(self.elportal)
        self.logger.info("******** Select the Learner********")
        act.key_down(Keys.CONTROL).click(learnerone).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        # self.logger.info("******** Define Variable for Learner Two********")
        # learnertwo = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-10-opt-5"]')
        # two = self.dfc.learnSLT2()
        # self.logger.info("******** Define Variable for ActionChains********")
        # act = ActionChains(self.elportal)
        # self.logger.info("********Select Learner One from the Dropdown********")
        # act.click(learnerone)
        # act.click(one)
        # self.logger.info("********Select Learner Two from the Dropdown********")
        # act.click(learnertwo)
        # act.click(two)
        # self.logger.info("********Exit the Dropdown Menu********")
        # act.key_down(Keys.ESCAPE)
        # self.logger.info("********Confirm the ActionChains Actions********")
        # act.perform()
        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.clickSaveCloseBtn()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Add Learner by Selection Test is Successful********")









        # act.key_down(Keys.CONTROL)
        # self.elportal.find_element(By.XPATH, "//body/div[4]/div[2]/div/mbody/form/div").click()


        # one = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-opt-4"]')



        # two = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-opt-8"]')

