import time
import sys
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.LoginPage import LoginPage
from testScripts.check import elportal
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_AddLearnerSearch:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    learner = "london"

    logger = LogGen.loggen()

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.elportal = setup
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
        self.logger.info("******** Login Test is successful ********")

        self.logger.info("******** Verifying Scheduling Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.dfc = DfcPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        time.sleep(3)
        self.logger.info("******** Click DFC Rotations Menu ********")
        self.dfc.clickDFC()
        time.sleep(3)
        self.logger.info("******** Click Scheduling menu********")
        self.dfc.clickScheduling()
        time.sleep(3)
        self.dfc.selectRotation()
        time.sleep(3)
        self.dfc.addLearner()
        time.sleep(3)
        self.logger.info("********Switch to the Create a DFC Rotation Form********")
        self.elportal.switch_to.window(parentwindowid)
        time.sleep(3)
        self.elportal.find_element(By.XPATH, "//body/div[4]/div[2]/div/mbody/form/div").click()
        time.sleep(3)
        one = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-opt-4"]')
        time.sleep(3)
        two = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-opt-8"]')
        # self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-ts-control"]').send_keys("london")
        # time.sleep(3)
        # element = self.elportal.find_element(By.XPATH, '//*[@id="tomselect-6-opt-296"]').click()
        # dropdown_option = elportal.find_element(By.XPATH, '//div[@id="tomselect-6-opt-4"]')
        act = ActionChains(self.elportal)
        # time.sleep(3)
        # act.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        # time.sleep(2)
        # act.key_down(Keys.DOWN).perform()
        act.key_down(Keys.CONTROL) # Hold Multiple Elements before click
        act.click(one).click(two).perform() # Click the dele
         # Adjust XPath
        # act.move_to_element(dropdown_option).click().perform()
        # act.key_down(Keys.CONTROL).click(dropdown_option).key_up(Keys.CONTROL).perform()




        # self.dfc.learnerField()
        # self.dfc.learnerFieldFD(self.learner)
        # self.logger.info("******** Click Create Rotation Button********")
        # self.dfc.createRotation()
        # time.sleep(3)
        # self.logger.info("********Switch to the Create a DFC Rotation Form********")
        # self.elportal.switch_to.window(parentwindowid)
        # time.sleep(3)
        # self.logger.info("********Enter the Rotation Name********")
        # self.dfc.rotationName(self.rotatename)
        # time.sleep(3)
        # self.logger.info("******** Click the Site Dropdown********")
        # self.dfc.siteCLK()
        # time.sleep(3)
        # self.logger.info("******** Select a Site********")
        # self.dfc.selSite()
        # time.sleep(3)
        # self.logger.info("******** Click the Subtract Max Learners Button********")
        # self.dfc.maxLearnSubt()
        # time.sleep(3)
        # self.logger.info("******** Click the Add Max Learners Button********")
        # self.dfc.maxLearnAdd()
        # time.sleep(3)
        # self.logger.info("********Click the Assign Coordinator Dropdown********")
        # self.dfc.assignCoord()
        # time.sleep(3)
        # self.logger.info("******** Select a Coordinator********")
        # self.dfc.selCoord()
        # time.sleep(3)
        # self.logger.info("******** Click the Assign Faculty Dropdown********")
        # self.dfc.assignFaculty()
        # time.sleep(3)
        # self.logger.info("******** Select a Faculty********")
        # self.dfc.selfaculty()
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
        # self.logger.info("**********Create a Rotation is Successful********")














