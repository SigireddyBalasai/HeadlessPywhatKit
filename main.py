from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div")))
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id="app"]/div/div/div[3]/div[1]/div/div[2]/div/div/span/svg")))
ok = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div")
print(ok.screenshot("hello.png"))
driver.close()
