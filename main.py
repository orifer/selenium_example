from cmath import log
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# ======= Setting =============
user = "your_user"
password = "your_password"
# =============================

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com")

# Cookies pop up => Click on "Essential"
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()

# Filling in the Credentials
driver.implicitly_wait(0.5)
driver.find_element(By.NAME, value="username").send_keys(user)
driver.find_element(By.NAME, "password").send_keys(password)

# Click on the log-in button
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

# Wait to log in  
time.sleep(6)

# Click on the notification button
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()

# Go to post
driver.get("https://www.instagram.com/p/CgjdLf2ocs1/")

time.sleep(6)
driver.quit()