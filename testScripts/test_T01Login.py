import time
import sys
import os
import pytest
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen
# from Configurations.paths import ROOT_DIR

class Test_Login_ElPortal(BaseTest):

    # baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()
    #
    # logger = LogGen.loggen()

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        # self.logger.info("******** Verifying Login Test ********")
        # self.logger.info("******** Call the Browse Configuration ********")
        # self.elportal.implicitly_wait(10)
        # self.logger.info("******** Launch the Application URL ********")
        # self.elportal.get(self.baseURL)
        # self.logger.info("******** Define the LoginPage Driver ********")
        # self.elp = LoginPage(self.elportal)
        # self.logger.info("******** Click the Home Button ********")
        # self.elp.clickHomeButton()
        # time.sleep(3)
        # self.logger.info("******** Enter the Username ********")
        # self.elp.emailAddress(self.username)
        # time.sleep(3)
        # self.logger.info("******** Enter the Password ********")
        # self.elp.setPassword(self.password)
        # time.sleep(3)
        # self.logger.info("******** Click the Sign in Button********")
        # self.elp.clickSignin()
        self.logger.info("******** Login Test is successful ********")
        act_title = self.elportal.title
        self.logger.info("******** Assert Page Title ********")
        if act_title == "EL Portal - Nightingale College":
            assert True
            self.elportal.quit()
        else:
            self.elportal.save_screenshot("/Users/OluwasegunOjeyinka/PycharmProjects/Edu/Screenshots/Failed.png")
            self.elportal.close()
            assert False
        self.logger.info("Login Test is successful and assertion passed")