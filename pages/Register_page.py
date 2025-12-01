
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
def open_browser():
    global driver
    global wait

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait=WebDriverWait(driver,10)
    #driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.get(r"https://demo.automationtesting.in/FileUpload.html")
    driver.maximize_window()
    time.sleep(5)
def switch_or_select_Home():
    Home_link_xpath="//div[@class='navbar-collapse collapse navbar-right']/descendant::ul[1]/li[1]/a"
    print(wait.until(EC.presence_of_element_located((By.XPATH,Home_link_xpath))))

    #Home_link_xpath.click()