import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
elportal = webdriver.Chrome(service=service)

elportal.get("https://staging.elportal.nightingale.edu/")
elportal.maximize_window()

elportal.find_element(By.XPATH, "//a[normalize-space()='Click Here to Continue']").click()
time.sleep(3)
elportal.find_element(By.XPATH, "//input[@name='username']").send_keys("automationadmin@nightingale.edu")
time.sleep(3)
elportal.find_element(By.XPATH, "//input[@name='password']").send_keys("collab1234")
time.sleep(3)
elportal.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[3]/a/div').click()
time.sleep(3)
elportal.find_element(By.XPATH, "//span[normalize-space()='Scheduling']").click()
time.sleep(2)
elportal.find_element(By.XPATH, "//span[normalize-space()='St Nicholas Medical Center Post Acute (Orientation)']").click()
time.sleep(2)
elportal.find_element(By.XPATH, "//span[normalize-space()='Add Day']").click()
time.sleep(2)
elportal.find_element(By.XPATH, "//input[@id='asel_faculty-ts-control']").send_keys("Faculty Queen Veronica Herman")
time.sleep(2)
queen=elportal.find_element(By.XPATH, "//div[@id='asel_faculty-opt-51']")
time.sleep(2)
act = ActionChains(elportal)
act.key_down(queen).click().perform()
time.sleep(7)


#elportal.find_element(By.XPATH, "//span[normalize-space()='Learner Search']").click() Learner Search Element
#elportal.find_element(By.XPATH, "//button[@type='button']//*[name()='svg']").click()  # Semester Element

#elportal.find_element(By.XPATH, "//button[contains(text(),'Spring 2025')]").click()
#elportal.find_element(By.XPATH, "//button[contains(text(),'Fall 2025')]").click()
#elportal.find_element(By.XPATH, "//button[contains(text(),'Spring 2026')]").click()
# elportal.find_element(By.XPATH, "//button[contains(text(),'Summer 2026')]").click()
# elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[3]/a/div').click()  # DFC Element
# time.sleep(3)
# elportal.find_element(By.XPATH, "//span[normalize-space()='Scheduling']").click() # Scheduling

# elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[4]/a/div/div').click() # VCBC Mgt Element
# elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[5]/a/div/div').click() # Compliance Element
# elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[6]/a/div/div').click() # Practicum
# elportal.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[7]/a/div/div').click() # Settings
time.sleep(10)