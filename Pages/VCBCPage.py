from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class VCBCPage:

    def __init__(self, elportal):
        self.elportal = elportal

    def clickVCBCMgt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[4]/a/div'))).click()

    def createVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create VCBC']"))).click()

    def vcbcSessionName(self, sessionname):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(sessionname)

    def typeMakeup(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='makeup']"))).click()

    def typeRegular(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='regular']"))).click()

    def vcbcCourses(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmVCBCEditor"]/div[3]/div'))).click()

    def descriptionIframe(self):
        iframeext=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@class='rte-editable']")))
        self.elportal.switch_to.frame(iframeext)

    def enterDescription(self, description):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[@class='rte-toggleborder']"))).send_keys(description)

    def lookupCourse(self, coursepick):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-ts-control"]'))).send_keys(coursepick)

    def pickCourseMakeDFC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-3"]'))).click()

    def pickCourseReg1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-1"]'))).click()

    def pickCourseReg2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-2"]'))).click()

    def pickCourseReg3(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-3"]'))).click()

    def enterSlots(self, slot):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='slots']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='slots']"))).send_keys(slot)

    def liveAt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sm:col-span-3 flex flex-col']//input[@type='text']"))).click()

    def liveAtJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='0']"))).click()

    def liveAtFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='1']"))).click()

    def liveAtMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='2']"))).click()

    def liveAtApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='3']"))).click()

    def liveAtMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='4']"))).click()

    def liveAtOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='9']"))).click()

    def liveAtMonth(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//span[@class='flatpickr-next-month']"))).click()

    def liveMonth(self, month):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Month']"))).send_keys(month)

    def liveAtYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).send_keys(year)

    def liveAtDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='September 15, 2025']"))).click()

    def closeAt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[3]//input[2]"))).click()

    def closeAtYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).send_keys(year)

    def closeAtDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="dayContainer"]//span')))
        # WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='September 20, 2025']")))

    def liveHour(self, livehour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-hour']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-hour']"))).send_keys(livehour)

    def liveMinute(self, liveminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).send_keys(liveminute)

    def closeHour(self, closehour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[3]/div[1]/input"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[3]/div[1]/input"))).send_keys(closehour)

    def closeMinute(self, closeminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).send_keys(closeminute)

    def selLiveAM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar']//span[@title='Click to toggle'][normalize-space()='AM']"))).click()

    def selClosePM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//body/div[6]/div[3]/span[2]'))).click()

    def closeAtMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='2']"))).click()

    def closeAtOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='10']"))).click()

    def closeAtMonth(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//span[@class='flatpickr-next-month']"))).click()

    def dateField(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='w-full px-3']//input[@type='text']"))).click()

    def dateJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='0']"))).click()

    def dateFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='1']"))).click()

    def dateMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='2']"))).click()

    def dateApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='3']"))).click()

    def dateMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']option[@value='4']"))).click()

    def dateJun(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='5']"))).click()

    def dateJul(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='6']"))).click()

    def dateAug(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='7']"))).click()

    def dateSep(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='8']"))).click()

    def dateOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='9']"))).click()

    def dateNov(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='10']"))).click()

    def dateYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@aria-label='Year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@aria-label='Year']"))).send_keys(year)

    def date1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[6]"))).click()

    def date5(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[8]"))).click()

    def date10(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[13]"))).click()

    def date15(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[18]"))).click()

    def date20(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[23]"))).click()

    def date25(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[28]"))).click()

    def date30(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[33]"))).click()

    def date31(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[34]"))).click()

    def vcbcSaveChanges(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[4]/div[2]/div/mactions/div/button[2]"))).click()

    def publishtoFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Publish to Faculty']"))).click()

    def vcbcPubSuccess(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Close']"))).click()

    def singleVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[13]/td[6]/a[1]/span[1]"))).click()

    def allocateSlotBtn(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Assign Slots']"))).click()

    def selFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']"))).click()

    def facultyMs(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']/option[@value='51']"))).click()

    def facultyProfKerluke(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']/option[@value='32']"))).click()

    def facultyQueenBartell(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']/option[@value='29']"))).click()

    def allocateButton(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmAllocateSlot']"))).click()

    def allocateSlots(self, slot):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='slots']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='slots']"))).send_keys(slot)

    def btnVcbcSlot(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Slot #1']"))).click()

    def pickDate(self, driver, date_value):
        alldates = driver.find_elements(By.XPATH, '//div[@class="dayContainer"]//span')
        for datepick in alldates:
            if datepick.text == date_value:
                datepick.click()
                break
