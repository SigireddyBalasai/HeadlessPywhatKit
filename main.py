from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless") will open hedless means allow us to work without showing website
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0")
driver = webdriver.Chrome(options=chrome_options)


def login():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div")))
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div/div/span')))

    ok = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div")
    if not ok:
        return True
    print(ok.screenshot("hello.png"))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/div')))
    return True


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


def send_user_message(phone: str, message: str):
    phone = phone.split(" ", "")
    driver.get(f'https://web.whatsapp.com/send?phone={phone}&message={message}')
    element = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    element.click()


search('hello')
driver.close()
