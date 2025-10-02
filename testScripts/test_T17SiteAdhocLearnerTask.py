import time
import sys
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from testScripts.base_test import BaseTest


class Test_Site_Adhoc_Learner_Task(BaseTest):

    site  = "St Nicholas Medical Center"
    name = "Preceptor Welcome Session"
    note = "Preceptor Discussion"
    dline = "4"
    subject = "Preceptor Engagement"
    # siteaddress = "12 Nicholas Drive North Alpine, AK 99903"
    email= "Preceptor 101"
    # intnote = "Find the right care for you"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Site Adhoc Learner Task Test********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        self.logger.info("******** Click Sites menu********")
        self.dfc.clickSites()
        self.logger.info("******** Search for a Site********")
        self.dfc.fieldSearchSite(self.site)
        # self.elportal.switch_to.window(parentwindowid)
        time.sleep(3)
        self.logger.info("******** Click the Site View Button********")
        self.dfc.btnViewSite()
        self.logger.info("******** Click the Create Adhoc Task Button on Site's Details Page********")
        self.dfc.btnSiteCreateAdhocTask()
        self.logger.info("********Switch to the Assign Task to Site Modal********")
        self.logger.info("******** Click the Available Tasks Field********")
        self.dfc.fieldCreateAdhocTaskName(self.name)
        self.logger.info("********Select Target Option from the Dropdown********")
        self.dfc.fieldTargetLearnerExt()
        self.logger.info("********Enter the Deadline Days********")
        self.dfc.fieldDeadline(self.dline)
        self.logger.info("********Select Attachment Required Option from the Dropdown********")
        self.dfc.fieldAttachmentRequiredAny()
        self.logger.info("********Select Type Option from the Dropdown********")
        self.dfc.fieldTypeDfc()
        self.logger.info("******** Enter Task Description********")
        self.dfc.fieldDescription(self.note)
        self.logger.info("******** Enter the Email Subject********")
        self.dfc.fieldEmailSubject(self.subject)
        self.logger.info("******** Switch to the External Notes' Iframe********")
        self.dfc.fieldEmailContentIframe()
        self.logger.info("******** Enter the External Notes********")
        self.dfc.enterEmailContent(self.email)
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Save and Close Button********")
        self.dfc.btnSaveClose()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********Edit Site Test is Successful********")





