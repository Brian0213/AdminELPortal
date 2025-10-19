import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_Create_Sites(BaseTest):

    sitename  = "Ronald Reagan UCLA Medical Center"
    siteaddress = "757 Westwood Plaza, Los Angeles, CA 90095"
    extnote = "Committed to medical excellence through outstanding patient care, leadership in research, and education, while maintaining a compassionate environment."
    intnote = "Committed to medical excellence through outstanding patient care, leadership in research, and education, while maintaining a compassionate environment."


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
        self.logger.info("******** Click SOFEs menu********")
        self.dfc.clickSites()
        self.logger.info("******** Click Create SOFEs Button********")
        self.dfc.createSite()
        self.logger.info("********Switch to the Create SOFEs Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.dfc.siteName(self.sitename)
        self.dfc.sofeJuneau()
        self.dfc.terriSouthWest()
        self.dfc.timeZoneHonolulu()
        self.dfc.siteAddress(self.siteaddress)
        self.logger.info("******** Switch to the External Notes' Iframe********")
        self.dfc.externalIframe()
        self.logger.info("******** Enter the External Notes********")
        self.dfc.enterExternalNote(self.extnote)
        self.logger.info("******** Switch back to the Create Site form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Internal Notes Tab********")
        self.dfc.clickInternalNotes()
        self.logger.info("******** Switch to the Internal Notes' Iframe********")
        self.dfc.internalIframe()
        self.logger.info("******** Enter the Internal Notes********")
        self.dfc.enterInternalNote(self.intnote)
        self.logger.info("******** Switch back to the Create Site form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Save & Close Button********")
        self.dfc.siteSaveClose()
        self.logger.info("******** Close the Browser********")
        self.elportal.quit()
        self.logger.info("**********Create Site Test is Successful********")

