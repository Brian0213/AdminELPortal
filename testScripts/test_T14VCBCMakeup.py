import time
import sys
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.VCBCPage import VCBCPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest


class Test_Create_VCBC_Makeup(BaseTest):

    sessionname  = "Mental Health Nursing"
    coursepick = "an"
    description = "Find the right care for you"
    slot = "3"
    year ="2025"
    livehour = "10"
    closehour = "4"
    month = "September"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying VCBCs Makeup Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        act = ActionChains(self.elportal)
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.vcb.clickVCBCMgt()
        self.logger.info("******** Click Create VCBCs Button********")
        self.vcb.createVCBC()
        self.logger.info("********Switch to the Create VCBCs Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Switch to the Create SOFEs Form********")
        self.elportal.switch_to.window(parentwindowid)
        self.logger.info("********Enter the Session Name********")
        self.vcb.vcbcSessionName(self.sessionname)
        self.logger.info("********Select the Session Type Makeup********")
        self.vcb.typeMakeup()
        self.logger.info("******** Click the Course Field********")
        self.vcb.vcbcCourses()
        self.logger.info("******** Lookup Course********")
        self.vcb.pickCourseReg1()
        self.logger.info("******** Select Course ********")
        self.vcb.pickCourseReg3()
        self.logger.info("******** Switch to the Notes' Iframe********")
        self.vcb.descriptionIframe()
        self.logger.info("******** Enter the Notes********")
        self.vcb.enterDescription(self.description)
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.logger.info("******** Click the Date Field********")
        self.vcb.dateField()
        self.logger.info("******** Select the Date Month********")
        self.vcb.dateOct()
        self.logger.info("******** Select the Date Year********")
        self.vcb.dateYear(self.year)
        self.logger.info("******** Select the Date Number********")
        self.vcb.pickDate(self.elportal, '5')
        self.logger.info("******** Enter Number of Slots********")
        self.vcb.enterSlots(self.slot)
        self.logger.info("******** Select the Live At Hour********")
        self.vcb.liveAt()
        self.logger.info("******** Select the Live At Month********")
        self.vcb.liveAtMonth()
        self.logger.info("******** Select the Live At Year********")
        self.vcb.liveAtYear(self.year)
        self.logger.info("******** Select the Live At Date********")
        self.vcb.pickDate(self.elportal, '13')
        self.logger.info("******** Select the Live At Hour********")
        self.vcb.liveHour(self.livehour)
        self.elportal.find_element(By.XPATH, '//*[@id="frmVCBCEditor"]/div[6]/div[3]/input[2]').click()
        # self.logger.info("******** Select Live At AM/PM*******")
        # self.vcb.selLiveAM()
        self.logger.info("******** Click the Close At Field********")
        self.vcb.closeAt()
        self.logger.info("******** Select the Close At Month********")
        self.vcb.closeAtMonth()
        self.logger.info("******** Select the Close At Year********")
        self.vcb.closeAtYear(self.year)
        self.logger.info("******** Select the Close At Date********")
        self.vcb.pickDate(self.elportal, '23')
        self.logger.info("******** Select the Close Hour********")
        self.vcb.closeHour(self.closehour)
        self.logger.info("******** Click the Save Changes Button********")
        self.vcb.vcbcSaveChanges()
        self.logger.info("******** Close the Browser********")
        self.elportal.close()
        self.logger.info("**********MakeUp VCBCs Creation Test is Successful********")
















        # alldates=self.elportal.find_elements(By.XPATH, '//div[@class="dayContainer"]//span')
        # for datepick in alldates:
        #     date=datepick.text
        #     if date=='10':
        #         datepick.click()
        #         break




















        # self.elportal.find_element(By.XPATH, '//*[@id="frmVCBCEditor"]/div[6]/div/div/input[2]').click() # Dates
        # time.sleep(2)
        # self.elportal.find_element(By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='2']").click() # Month
        # time.sleep(2)
        # self.elportal.find_element(By.XPATH, "//div[7]/div[1]/div/div/div/input").clear()
        # self.elportal.find_element(By.XPATH, "//div[7]/div[1]/div/div/div/input").send_keys("2026") # Year
        # time.sleep(2)
        # self.elportal.find_element(By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[20]").click() # Day

        # self.elportal.find_element(By.XPATH, '//*[@id="frmVCBCEditor"]/div[3]/div').click()
        # time.sleep(3)
        # self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-ts-control"]').send_keys("repell")
        # time.sleep(2)
        # self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-opt-16"]').click()







