import sys
from datetime import date
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


s = Service('/usr/local/src/chromedriver')
s.start()
driver = webdriver.Remote(s.service_url)
driver.implicitly_wait(10)


def download_current():
    driver.get("https://<company>.sharepoint.com/:f:/s/group/Eh2kR4f0cbVPr3JVHmdbkh8BEcJte5ITOZ11UucqDnK_0A?e=oxPECV")
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/button/span')))
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/i[2]").click()
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/button/span')))
    print("button visible")
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/button/span").click()

def login():
    download_current()
    time.sleep(30)
    driver.quit()
