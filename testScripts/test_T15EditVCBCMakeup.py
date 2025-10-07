import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.VCBCPage import VCBCPage
from testScripts.base_test import BaseTest


class Test_Edit_VCBC_Makeup(BaseTest):

    sessionname  = "Working Session for Community Centers"
    coursepick = "repell"
    description = "Find the right care for you"
    slot = "5"
    year ="2026"
    livehour = "9"
    closehour = "5"


    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)
        self.logger.info("******** Verifying VCBCs Makeup Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.vcb = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.elp.semesterNav()
        time.sleep(2)
        self.elp.semesSpring()
        time.sleep(3)
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.vcb.clickVCBCMgt()
        time.sleep(3)
        self.elportal.find_element(By.XPATH, "//tbody/tr[13]/td[6]/a[1]/span[1]").click()
        # self.logger.info("******** Click Create VCBCs Button********")
        # self.vcb.createVCBC()
        # time.sleep(3)
        # self.logger.info("********Switch to the Create VCBCs Form********")
        # self.elportal.switch_to.window(parentwindowid)
        # time.sleep(3)
        # self.logger.info("********Switch to the Create SOFEs Form********")
        # self.elportal.switch_to.window(parentwindowid)
        # time.sleep(3)
        # self.logger.info("********Enter the Session Name********")
        # self.vcb.vcbcSessionName(self.sessionname)
        # time.sleep(3)
        # self.logger.info("********Select the Session Type Makeup********")
        # self.vcb.typeMakeup()
        # time.sleep(3)
        # self.vcb.vcbcCourses()
        # time.sleep(3)
        # self.vcb.lookupCourse(self.coursepick)
        # time.sleep(3)
        # self.vcb.pickCourseMake()
        # time.sleep(3)
        # self.logger.info("******** Switch to the Notes' Iframe********")
        # self.vcb.descriptionIframe()
        # self.logger.info("******** Enter the Notes********")
        # self.vcb.enterDescription(self.description)
        # time.sleep(3)
        # self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        # self.elportal.switch_to.default_content()
        # time.sleep(2)
        # self.vcb.enterSlots(self.slot)
        # time.sleep(2)
        # self.vcb.liveAt()
        # time.sleep(2)
        # self.vcb.liveAtMar()
        # time.sleep(2)
        # self.vcb.liveAtYear(self.year)
        # time.sleep(2)
        # self.vcb.liveAtDay()
        # time.sleep(2)
        # self.vcb.liveHour(self.livehour)
        # time.sleep(2)
        # self.vcb.selLiveAM()
        # time.sleep(2)
        # self.vcb.closeAt()
        # time.sleep(2)
        # self.vcb.closeAtMar()
        # time.sleep(2)
        # self.vcb.closeAtYear(self.year)
        # time.sleep(2)
        # self.elportal.find_element(By.XPATH, "//body/div[6]/div[2]/div/div[2]/div/span[21]").click()
        # # self.vcb.closeAtDay()
        # time.sleep(2)
        # self.vcb.closeHour(self.closehour)
        # time.sleep(2)
        # self.vcb.dateField()
        # time.sleep(2)
        # self.vcb.dateMar()
        # time.sleep(2)
        # self.vcb.dateYear(self.year)
        # time.sleep(2)
        # self.vcb.date1()
        # time.sleep(2)
        # self.vcb.vcbcSaveChanges()


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







