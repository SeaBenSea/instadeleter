from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.instagram.com')

wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/div[2]/button')))
loginbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[2]/button')
loginbutton.click()

girdi = input("Başlamak için sil yazınız: ")
if(girdi == "sil"): 
    f = open("linkler.txt", "r")
    for x in f:
        driver.get(x)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/div/article/div[1]/button')))
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[1]/button').click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/button[1]')))
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[1]').click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/button[1]')))
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[1]').click()
        time.sleep(2)
    f.close()
else:
    print("Çıkış yapılıyor.")
    driver.quit()
