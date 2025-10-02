import time
import sys
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from testScripts.check import elportal
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Scheduling(BaseTest):

    rotatename = "Travel Outreach Orientation"
    month = "November"
    year = "2025"
    starthour = "9"
    startminute = "30"
    endhour = "5"
    extnote = "Preceptors Notes"
    intnote = "Preceptee's Todo On The First Day"
    siteabbrev = "St Colin's"

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
        # self.elportal.find_element(By.XPATH, "//input[@id='asel_site-ts-control']").send_keys("St Nicholas")
        self.dfc.siteSearch(self.siteabbrev)
        self.logger.info("******** Select a Site********")
        self.dfc.siteSelect()
        self.logger.info("******** Click the Subtract Max Learners Button********")
        self.dfc.maxLearnSubt()
        self.logger.info("******** Click the Add Max Learners Button********")
        self.dfc.maxLearnAdd()
        self.logger.info("********Click the Assign Coordinator Dropdown********")
        self.dfc.assignCoord()

        # self.logger.info("******** Select a Coordinator********")
        # self.dfc.coordSele()
        # time.sleep(3)
        # self.logger.info("******** Click the Assign Faculty Dropdown********")
        # self.dfc.assignFaculty()
        # time.sleep(3)
        # self.logger.info("******** Select a Faculty********")
        # self.dfc.facultySel()
        # time.sleep(3)
        # self.dfc.rotationDays()
        # time.sleep(3)
        # self.logger.info("******** Select Year********")
        # self.dfc.selYear(self.year)
        # time.sleep(3)
        # self.logger.info("******** Select Month********")
        # self.dfc.selMonth(self.month)
        # self.logger.info("******** Select Day********")
        # self.dfc.selDay()
        # time.sleep(3)
        # self.logger.info("******** Click the Live Date Calendar********")
        # self.dfc.liveDate()
        # time.sleep(3)
        # self.logger.info("******** Select Live Date Month********")
        # self.dfc.liveMonthFeb()
        # time.sleep(3)
        # self.logger.info("********Select Live Date Year*******")
        # self.dfc.liveYear(self.year)
        # time.sleep(3)
        # self.logger.info("******** Select the Live Date********")
        # self.dfc.liveDay()
        # self.logger.info("********Enter the Start Time********")
        # self.dfc.startHour(self.starthour)
        # time.sleep(3)
        # self.logger.info("********Enter the Start Minute********")
        # self.dfc.startMinute(self.startminute)
        # time.sleep(3)
        # self.logger.info("********Enter the End hour********")
        # self.dfc.endHour(self.endhour)
        # time.sleep(3)
        # self.logger.info("******** Select End option PM********")
        # self.dfc.selEndPM()
        # time.sleep(3)
        # self.logger.info("******** Switch to the External Notes' Iframe********")
        # self.dfc.externalIframe()
        # self.logger.info("******** Enter the External Notes********")
        # self.dfc.enterExternalNote(self.extnote)
        # time.sleep(3)
        # self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        # self.elportal.switch_to.default_content()
        # time.sleep(2)
        # self.logger.info("******** Click the Internal Notes Tab********")
        # self.dfc.clickInternalNotes()
        # time.sleep(3)
        # self.logger.info("******** Switch to the Internal Notes' Iframe********")
        # self.dfc.internalIframe()
        # time.sleep(3)
        # self.logger.info("******** Enter the Internal Notes********")
        # self.dfc.enterInternalNote(self.intnote)
        # time.sleep(3)
        # self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        # self.elportal.switch_to.default_content()
        # time.sleep(3)
        # self.logger.info("******** Click the Save & Close Button********")
        # self.dfc.clickSaveCloseBtn()
        # time.sleep(5)
        # self.logger.info("******** Close the Browser********")
        # self.elportal.close()
        # self.logger.info("**********Create a Rotation Test is Successful********")














