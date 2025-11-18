import time
from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PracticumPage:

    def __init__(self, elportal):
        self.elportal = elportal

    def emailAddress(self, emailaddress):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(emailaddress)

    def setPassword(self, setpassword):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(setpassword)

    def clickPracticumTab(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/div/div/ul/li[2]/a'))).click()

    def btnBulkSpecialistAssign(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn bg-gray-900 text-gray-100 hover:bg-gray-700']"))).click()

    def btnDownloadUnassignedLearners(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Download Unassigned Learners']"))).click()

    def btnAssignSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[9]/td[7]/div[1]/div[2]/button[1]//*[name()='svg']"))).click()

    def fieldAssignSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='sel_site-ts-control']"))).click()

    def btnAssignSite1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="practicum-table"]/div[1]/pbody/div/table/tbody/tr[3]/td[7]/div/div[2]/button'))).click()

    def fieldAssignSite2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='sel_site-ts-control']"))).click()

    def fieldExpectedHours(self, hour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='hours']"))).send_keys(hour)

    def fieldTentativeDates(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='w-full form-input form-control input']"))).click()

    def selYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='numInput cur-year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='numInput cur-year']"))).send_keys(year)

    def pickDate(self, driver, date_value):
        alldates = driver.find_elements(By.XPATH, '//div[@class="dayContainer"]//span')
        for datepick in alldates:
            if datepick.text == date_value:
                datepick.click()
                break

    def fieldFromDate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[1]//input[2]"))).click()

    def fieldToDate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "// mbody // div[2] // input[2]"))).click()

    def btnAssign(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Assign']"))).click()

    def learnerAssignSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-sm bg-white border border-primary-400 hover:border-gray-700 text-primary-800']"))).click()

    def fieldLearnerSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[4]/div[2]/div/mbody/div/div[1]/div"))).click()

    def enterLearnerSite(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//div[@data-value='117']"))).click()

    def enterExpectedHours(self, hour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//div[@data-value='117']"))).send_keys(hour)

    def tabGraduate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Graduate']"))).click()

    def tabUnderGrad(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Undergrad']"))).click()

