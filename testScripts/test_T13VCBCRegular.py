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

class Test_Create_VCBC_Regular(BaseTest):

    sessionname  = "Capstone Competency Review"
    coursepick = "con"
    description = "Capstone Competency Introduction"
    slot = "3"
    year ="2025"
    livehour = "7"
    closehour = "3"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Regular VCBCs Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click VCBC Management Menu ********")
        self.vcb.clickVCBCMgt()
        self.logger.info("******** Click Create VCBCs Button********")
        self.vcb.createVCBC()
        self.logger.info("********Switch to the Create VCBCs Form********")
        self.elportal.switch_to.window(parentwindowid)
        # self.logger.info("********Switch to the Create SOFEs Form********")
        # self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Enter the Session Name********")
        self.vcb.vcbcSessionName(self.sessionname)
        self.logger.info("******** Click the Course Field********")
        self.vcb.vcbcCourses()
        self.logger.info("******** Select Course 1********")
        self.vcb.pickCourseReg1()
        # self.logger.info("******** Select Course 2********")
        # self.vcb.pickCourseReg2()
        self.logger.info("******** Switch to the Notes' Iframe********")
        self.vcb.descriptionIframe()
        self.logger.info("******** Enter the Notes********")
        self.vcb.enterDescription(self.description)
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Enter Number of Slots********")
        self.vcb.enterSlots(self.slot)
        self.logger.info("******** Select the Live At Hour********")
        self.vcb.liveAt()
        # self.logger.info("******** Select the Live At Month********")
        self.vcb.liveAtOct()
        # self.logger.info("******** Select the Live At Year********")
        # self.vcb.liveAtYear(self.year)
        self.logger.info("******** Select the Live At Date********")
        self.vcb.pickDate(self.elportal, '21')
        self.logger.info("******** Select the Live At Hour********")
        self.vcb.liveHour(self.livehour)
        self.logger.info("******** Select Live At AM/PM*******")
        # self.vcb.selLiveAM()
        self.logger.info("******** Click the Close At Field********")
        self.vcb.closeAt()
        self.logger.info("******** Select the Close At Month********")
        self.vcb.closeAtOct()
        # self.logger.info("******** Select the Close At Year********")
        # self.vcb.closeAtYear(self.year)
        self.logger.info("******** Select the Close At Number********")
        self.vcb.pickDate(self.elportal, '28')
        self.logger.info("******** Select the Close Hour********")
        self.vcb.closeHour(self.closehour)
        self.logger.info("******** Click the Date Field********")
        self.vcb.dateField()
        self.logger.info("******** Select the Date Month********")
        self.vcb.dateNov()
        self.logger.info("******** Select the Date Year********")
        self.vcb.dateYear(self.year)
        self.logger.info("******** Select the Date Number********")
        self.vcb.pickDate(self.elportal, '10')
        self.logger.info("******** Click the Save Changes Button********")
        self.vcb.vcbcSaveChanges()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Regular VCBCs Creation Test is Successful********")










