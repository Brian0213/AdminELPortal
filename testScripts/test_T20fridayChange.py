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

    sessionname  = "Practicum Orientation"
    coursepick = "cup"
    description = "Technology and Informatics"
    slot = "3"
    year ="2025"
    livehour = "8"
    closehour = "4"


    @pytest.mark.skip(reason="Skipping this test for now")
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)


        self.logger.info("******** Verifying Regular VCBCs Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.vcb.clickVCBCMgt()
        self.vcb.createVCBC()

        self.vcb.vcbcSessionName(self.sessionname)
        self.vcb.typeMakeup()
        self.vcb.vcbcCourses()
        self.vcb.lookupCourse(self.coursepick)
        self.vcb.pickCourseMakeDFC()

        self.vcb.descriptionIframe()
        self.vcb.enterDescription(self.description)
        self.elportal.switch_to.default_content()

        self.vcb.enterSlots(self.slot)

        # Live At
        self.vcb.liveAt()
        self.vcb.liveAtOct()
        self.vcb.liveAtYear(self.year)
        self.vcb.pickDate(self.elportal, '21')
        self.vcb.liveHour(self.livehour)
        self.vcb.selLiveAM()

        # Close At
        self.vcb.closeAt()
        self.vcb.closeAtOct()
        self.vcb.closeAtYear(self.year)
        self.vcb.pickDate(self.elportal, '21')
        self.vcb.closeHour(self.closehour)

        # Date Field
        self.vcb.dateField()
        self.vcb.dateOct()
        self.vcb.dateYear(self.year)
        self.vcb.pickDate(self.elportal, '5')
        time.sleep(5)

        self.vcb.vcbcSaveChanges()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********MakeUp VCBCs Creation Test is Successful********")

