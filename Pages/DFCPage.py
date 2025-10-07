from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DfcPage:

    def __init__(self, elportal):
        self.elportal = elportal
        self.act = ActionChains(self.elportal)

    def clickDFC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[3]/a/div'))).click()

    def clickScheduling(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Scheduling']"))).click()

    def clickCoordination(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Coordination']"))).click()

    def clickSOFE(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='SOFEs']"))).click()

    def clickSites(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sites']"))).click()

    def clickTaskTemp(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Task Templates']"))).click()

    def createRotation(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create Rotation']"))).click()

    def rotationName(self, rotatename):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(rotatename)

    def siteCLK(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex flex-col w-2/3']//div[@class='ts-control']"))).click()

    # def siteSear(self):
    #     WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex flex-col w-2/3']//div[@class='ts-control']"))).click()

    def siteSearch(self, siteabbrev):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='asel_site-ts-control']"))).send_keys(siteabbrev)

    def siteSearch3(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='dfc_sites-opt-73']"))).click()

    def siteSearch2(self, siteabbrev):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='dfc_sites']"))).send_keys(siteabbrev)

    def selSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='dfc_sites-opt-258']"))).click()

    def siteSelect(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='1001']"))).click()

    def siteSelect2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='73']"))).click()

    def maxLearnSubt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='subtract']"))).click()

    def maxLearnAdd(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='add']"))).click()

    def assignCoord(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-wrapper single required invalid']//div[@class='ts-control']"))).click()

    def lookupCoord(self, coordname):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='aslr_coordinator-ts-control']"))).send_keys(coordname)

    def selCoord(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='75']"))).click()

    def coordSele(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='92']"))).click()

    def assignFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex flex-col col-span-3']//div[@class='ts-wrapper single']//div[@class='ts-control']"))).click()

    def selfaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='aslr_faculty_id-opt-1']"))).click()

    def lookupFaculty(self, facultyname):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select A Faculty']"))).send_keys(facultyname)

    def facultySel(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='34']"))).click()

    def selMonth(self, month):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Month']"))).send_keys(month)

    def selYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='numInput cur-year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='numInput cur-year']"))).send_keys(year)

    def rotationDays(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex flex-col col-span-full']//input[@type='text']"))).click()

    def selDay3(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='October 15, 2025']"))).click()

    def selDay2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='October 14, 2025']"))).click()

    def selDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='October 13, 2025']"))).click()

    def liveDate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-span-2']//input[@type='text']"))).click()

    def liveMonthJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='0']"))).click()

    def liveMonthFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='1']"))).click()

    def liveMonthMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='2']"))).click()

    def liveMonthApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='3']"))).click()

    def liveMonthMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='4']"))).click()

    def liveMonthJun(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='5']"))).click()

    def liveMonthSep(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='8']"))).click()

    def liveMonthOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='9']"))).click()

    def liveYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/div/input"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/div/input"))).send_keys(year)

    def liveDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='October 12, 2025']"))).click()
        #WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='October 9, 2025']"))).click()

    def startHour(self, starthour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[1]/div/div/div/div/div[1]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[1]/div/div/div/div/div[1]/input'))).send_keys(starthour)

    def startMinute(self, startminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[1]/div/div/div/div/div[2]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[1]/div/div/div/div/div[2]/input'))).send_keys(startminute)

    def endHour(self, endhour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[3]/div/div/div/div/div[1]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[3]/div/div/div/div/div[1]/input'))).send_keys(endhour)

    def endMinute(self, endminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[3]/div/div/div/div/div[2]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[3]/div/div/div/div/div[2]/input'))).send_keys(endminute)

    def selStartPM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[1]/div/div/div/div/span[2]'))).click()

    def selEndPM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmCreateRotation"]/div[3]/div[4]/div[3]/div/div/div/div/span[2]'))).click()

    def externalIframe(self):
        iframeext=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='ngltbl_external_notes']//iframe[@class='rte-editable']")))
        self.elportal.switch_to.frame(iframeext)

    def enterExternalNote(self, extnote):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[@class='rte-toggleborder']"))).send_keys(extnote)

    def clickInternalNotes(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Internal Notes']"))).click()

    def internalIframe(self):
        iframeint=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='ngltbl_internal_notes']//iframe[@class='rte-editable']")))
        self.elportal.switch_to.frame(iframeint)

    def enterInternalNote(self, intnote):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[@class='rte-toggleborder']"))).send_keys(intnote)

    def clickSaveCloseBtn(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def selectRotation(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Critical Care/ICU']"))).click()

    def addDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Day']"))).click()

    def clickFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-wrapper single']//div[@class='ts-control']"))).click()

    def addFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="asel_faculty-opt-4"]'))).click()     # (FacultyOptions: 1-26)

    def addFaculty1(self):
        self.elportal.find_element(By.XPATH, '//*[@id="asel_faculty-opt-3"]').click()

    def addDFCDate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='rounded-md border-2 border-slate-300 form-control input']"))).click()

    def dFCMonthJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='0']"))).click()

    def dFCMonthFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='1']"))).click()

    def dFCMonthMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='2']"))).click()

    def dFCMonthApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='3']"))).click()

    def dFCMonthMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='4']"))).click()

    def dFCMonthJun(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='5']"))).click()

    def dFCMonthSep(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='8']"))).click()

    def dFCMonthOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='9']"))).click()

    def dFCMonthNov(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/select/option[@value='10']"))).click()

    def addDFCYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/div/input"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[5]/div[1]/div/div/div/input"))).send_keys(year)

    def addDFCDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='September 20, 2025']"))).click()

    def dfcStartHour(self, dfchour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[2]/div/div/div/div[1]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[2]/div/div/div/div[1]/input'))).send_keys(dfchour)

    def dfcStartMinute(self, dfcminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[2]/div/div/div/div[2]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[2]/div/div/div/div[2]/input'))).send_keys(dfcminute)

    def dfcEndHour(self, dfcendhour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[3]/div/div/div/div[1]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[3]/div/div/div/div[1]/input'))).send_keys(dfcendhour)

    def dfcEndMinute(self, dfcendmin):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[3]/div/div/div/div[2]/input'))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[3]/div/div/div/div[2]/input'))).send_keys(dfcendmin)

    def dfcselPM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmEditDay"]/div[3]/div[3]/div/div/div/span[2]'))).click()

    # def addLearner(self):
    #     WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div/div[@x-ref='contentarea']/div/div/div/div/div/button[2]"))).click()

    def learnerFieldFD(self, learner):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-5-ts-control"]'))).send_keys(learner)

    def learnerField(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//body/div[4]/div[2]/div/mbody/form/div'))).click()

    def pubtoFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Publish to Faculty']"))).click()

    def startCoordination(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Start Coordination']"))).click()

    def addLearner(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Learner']"))).click()

    def Learner(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Learner']"))).click()

    def learnSLT1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-3"]'))).click()

    def learnSLT2(self):
       WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-7-opt-2"]'))).click()

    def learnSLT3(self):
       WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-7-opt-4"]'))).click()


    def learnSRC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-5-opt-237"]'))).click()

    def createSOFE(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn bg-gray-900 text-gray-100 hover:bg-gray-800']"))).click()

    def sofeName(self, sofename):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(sofename)

    def sofeState(self, sofestate):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='state']"))).send_keys(sofestate)

    def sofeNotes(self, sofenotes):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[@class='rte-toggleborder']"))).send_keys(sofenotes)

    def notesIframe(self):
        iframeint=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@class='rte-editable']")))
        self.elportal.switch_to.frame(iframeint)

    def sofeSaveClose(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save & Close']"))).click()

    def createSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create Site']"))).click()

    def siteName(self, sitename):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(sitename)

    def siteAddress(self, siteaddress):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@name='address']"))).send_keys(siteaddress)

    def sofeOlympia(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sofe']/option[@value='1']"))).click()

    def sofeSacramento(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sofe']/option[@value='2']"))).click()

    def sofeJuneau(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sofe']/option[@value='3']"))).click()

    def sofeSaltLakeCity(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sofe']/option[@value='4']"))).click()

    def terriNorthEast(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='territory_id']/option[@value='1']"))).click()

    def terriSouthEast(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='territory_id']/option[@value='2']"))).click()

    def terriNorthWest(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='territory_id']/option[@value='3']"))).click()

    def terriSouthWest(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='territory_id']/option[@value='4']"))).click()

    def timeZoneAmeriDenver(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='America/Denver']"))).click()

    def timeZoneAmeriChicago(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='America/Chicago']"))).click()

    def timeZoneAmeriNewYork(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='America/New_York']"))).click()

    def timeZoneLosAngeles(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='America/Los_Angeles']"))).click()

    def timeZoneAnchorage(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='America/Anchorage']"))).click()

    def timeZoneAdak(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='America/Adak']"))).click()

    def timeZoneHonolulu(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='timezone']/option[@value='Pacific/Honolulu']"))).click()

    def siteSaveClose(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@allow_scroll='yes']"))).click()

    def editFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='dfc1030']//button[@hx-target='body']//*[name()='svg']"))).click()

    def publishtoFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Publish to Faculty']"))).click()

    def vcbcPubSuccess(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Close']"))).click()

    def rotationTransfer(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//tr[@id='rotation-10']//span[contains(text(),'Transfer')]"))).click()

    def transferRotationSpec(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="specialist_id"]/option[@value="56"]'))).click()   #[Options=82,70,85]

    def btnTransferClose(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmTransferRotation']"))).click()

    def fieldAvailableTasks(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-wrapper multi']//div[@class='ts-control']"))).click()

    def taskBadgePhoto(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='task-opt-20']"))).click()  #Badge Photo

    def fieldType(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-wrapper single required']//div[@class='ts-control']"))).click()

    def typeBoth(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='both']"))).click()

    def typeDfc(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='dfc']"))).click()

    def typePracticum(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-value='practicum']"))).click()

    def fieldSearchSite(self, site):
        lookup=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        lookup.send_keys(site)
        lookup.send_keys(Keys.RETURN)

    def btnViewSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[2]/div/div[2]/div[1]/pbody/div/table/tbody/tr/td[6]/a'))).click()

    def btnSiteAddTask(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Task']"))).click()

    def btnSiteCreateAddTask(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Task']"))).click()

    def btnAssignandClose(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Assign & Close']"))).click()

    def btnSiteCreateAdhocTask(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create Adhoc Task']"))).click()

    def fieldCreateAdhocTaskName(self, name):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(name)

    def fieldTargetLearnerInternal(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='internal']"))).clear()

    def fieldTargetLearnerExternal(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='external']"))).clear()

    def fieldTargetFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='faculty']"))).clear()

    def fieldTargetFacultyInternal(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='faculty-internal']"))).clear()

    def fieldTarget(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex gap-3']//div[1]"))).clear()

    def fieldDeadline(self, dline):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='deadline']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='deadline']"))).send_keys(dline)

    def fieldTypePracticum(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='type']/option[@value='practicum']"))).click()

    def fieldTypeBoth(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='type']/option[@value='both']"))).click()

    def fieldTypeDfc(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='type']/option[@value='dfc']"))).click()

    def fieldTargetFacultyInternal(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='faculty-internal']"))).click()

    def fieldTargetFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='faculty']"))).click()

    def fieldTargetLearnerExt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='external']"))).click()

    def fieldTargetLearnerInt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='target']/option[@value='internal']"))).click()

    def fieldAttachmentRequiredNone(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='attachment_type']/option[@value='none']"))).click()

    def fieldAttachmentRequiredDoc(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='attachment_type']/option[@value='document']"))).click()

    def fieldAttachmentRequiredMedia(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='attachment_type']/option[@value='media']"))).click()

    def fieldAttachmentRequiredAny(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='attachment_type']/option[@value='any']"))).click()

    def fieldDescription(self, note):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='note']"))).send_keys(note)

    def fieldEmailSubject(self, subject):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email_subject']"))).send_keys(subject)

    def fieldEmailContentIframe(self):
        iframeint=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@class='rte-editable']")))
        self.elportal.switch_to.frame(iframeint)

    def enterEmailContent(self, email):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[@class='rte-toggleborder']"))).send_keys(email)

    def btnSaveClose(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save & Close']"))).click()

    def pickDate(self, driver, date_value):
        alldates = driver.find_elements(By.XPATH, '//div[@class="dayContainer"]//span')
        for datepick in alldates:
            if datepick.text == date_value:
                datepick.click()
                break
