import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Scheduling(BaseTest):

    rotatename = "Child Health Awareness"
    month = "November"
    year = "2025"
    starthour = "9"
    startminute = "30"
    endhour = "5"
    extnote = "Child Health Notes"
    intnote = "Child Health Awareness Orientation"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        # self.login(self.elportal)
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Call the Browse Configuration ********")
        self.elportal.implicitly_wait(10)
        self.logger.info("******** Launch the Application URL ********")
        self.elportal.get(self.baseURL)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)
        self.logger.info("******** Click the Home Button ********")
        self.elp.clickHomeButton()
        time.sleep(3)
        self.logger.info("******** Enter the Username ********")
        self.elp.emailAddress(self.username)
        time.sleep(3)
        self.logger.info("******** Enter the Password ********")
        self.elp.setPassword(self.password)
        time.sleep(3)
        self.logger.info("******** Click the Sign in Button********")
        self.elp.clickSignin()
        time.sleep(5)
        self.logger.info("******** Verifying Scheduling Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        self.logger.info("******** Click Create Rotation Button********")
        self.dfc.createRotation()
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Enter the Rotation Name********")
        self.dfc.rotationName(self.rotatename)
        self.logger.info("******** Click the Site Dropdown********")
        self.dfc.siteCLK()
        self.logger.info("******** Select a Site********")
        self.dfc.selSite()
        self.logger.info("******** Click the Subtract Max Learners Button********")
        self.dfc.maxLearnSubt()
        self.logger.info("******** Click the Add Max Learners Button********")
        self.dfc.maxLearnAdd()
        self.logger.info("********Click the Assign Coordinator Dropdown********")
        self.dfc.assignCoord()
        self.logger.info("******** Select a Coordinator********")
        self.dfc.selCoord()
        self.logger.info("******** Click the Assign Faculty Dropdown********")
        self.dfc.assignFaculty()
        self.logger.info("******** Select a Faculty********")
        self.dfc.selfaculty()
        self.dfc.rotationDays()
        self.logger.info("******** Select Year********")
        self.dfc.selYear(self.year)
        self.logger.info("******** Select Month********")
        self.dfc.selMonth(self.month)
        self.logger.info("******** Select Day********")
        self.dfc.pickDate(self.elportal, '14')
        self.logger.info("******** Click the Live Date Calendar********")
        self.dfc.liveDate()
        self.logger.info("******** Select Live Date Month********")
        self.dfc.liveMonthOct()
        self.logger.info("********Select Live Date Year*******")
        self.dfc.liveYear(self.year)
        self.logger.info("******** Select the Live Date********")
        self.dfc.pickDate(self.elportal, '9')
        self.logger.info("********Enter the Start Time********")
        self.dfc.startHour(self.starthour)
        self.logger.info("********Enter the Start Minute********")
        self.dfc.startMinute(self.startminute)
        self.logger.info("********Enter the End hour********")
        self.dfc.endHour(self.endhour)
        self.logger.info("******** Select End option PM********")
        self.dfc.selEndPM()
        self.logger.info("******** Switch to the External Notes' Iframe********")
        self.dfc.externalIframe()
        self.logger.info("******** Enter the External Notes********")
        self.dfc.enterExternalNote(self.extnote)
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Internal Notes Tab********")
        self.dfc.clickInternalNotes()
        self.logger.info("******** Switch to the Internal Notes' Iframe********")
        self.dfc.internalIframe()
        self.logger.info("******** Enter the Internal Notes********")
        self.dfc.enterInternalNote(self.intnote)
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.clickSaveCloseBtn()
        time.sleep(5)
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Create a Rotation Test is Successful********")














