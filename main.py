from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#chrome_options.add_argument("--headless") will open hedless means allow us to work without showing website
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0")
driver = webdriver.Chrome(options=chrome_options)


def login():
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div")))
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div/div/span')))
    ok = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div")
    print(ok.screenshot("hello.png"))


def search(text):
    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')))
    ok = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]")
    ok.click()
    ok.send_keys("+91 9398993400")
    ok.send_keys(Keys.ENTER)

def get_pending_chats():
    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/button/div/span')))
    ok = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/button/div/span")
    ok.click()
search('hello')
driver.close()
