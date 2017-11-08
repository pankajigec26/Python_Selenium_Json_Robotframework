from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
fp = webdriver.FirefoxProfile(r'D:\userdata\khchoudh\Desktop\1m5ho3ed.Selenium-P')
driver = webdriver.Firefox(fp)
driver.get("http://10.131.14.245:30016/index.html")

timeout = 160

#Login_page 
try:
element_present1 = EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
WebDriverWait(driver, timeout).until(element_present1)
except TimeoutException:
print "Timed out waiting for login page to load"
driver.find_element_by_xpath("//input[@name='username']").clear()
driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@name='password']").clear()
driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
driver.find_element_by_xpath("//button").click()
time.sleep(20)

#Selecting test case
driver.find_element_by_xpath(".//*[@id='side-menu']/li[5]/a").click()

try:
element_present = EC.presence_of_element_located((By.XPATH, "Element_presence"))
WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
print "Timed out waiting for page to load"

#Selecting drop downs 

driver.find_element_by_xpath("//span[text()='ms3-designboard rev.2016-10-17 ']/ancestor::a/i").click()

driver.find_element_by_xpath("//span[text()='operations ']/ancestor::a/i").click()

driver.find_element_by_xpath("//span[text()='saveScenario ']/ancestor::a/i").click()


try:
element_present3 = EC.presence_of_element_located((By.XPATH, "//input[@class='leaf-input form-control input-small ng-pristine ng-untouched ng-valid ng-scope']"))
WebDriverWait(driver, timeout).until(element_present3)
except TimeoutException:
print "Timed out waiting for input box"

#Filling text boxes
driver.find_element_by_xpath("//div[@id='pageContent']/div/div/div[6]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/input").send_keys("Test")
driver.find_element_by_xpath("//div[@id='pageContent']/div/div/div[6]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/input").send_keys("Sample")

