import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(r"https://demo.automationtesting.in/Windows.html")

driver.maximize_window()
wait =WebDriverWait(driver,10)
switch_to_link_xpath="//div[@class='navbar-collapse collapse navbar-right']/ul//a[text()='SwitchTo']"
switch_to_element=wait.until(EC.presence_of_element_located((By.XPATH,switch_to_link_xpath)))
#print(switch_to_element)
act=ActionChains(driver)
act.move_to_element(switch_to_element).perform()
time.sleep(5)

#
Frames_link_xpath="//ul[@class = 'nav navbar-nav']/descendant::a[text() = 'Frames']"
Frame_link_ele=driver.find_element(By.XPATH,Frames_link_xpath)
Frame_link_ele.click()

Iframe_xpath="//iframe[@id ='singleframe']"
Iframe_ele=driver.find_element(By.XPATH,Iframe_xpath)
driver.switch_to.frame(Iframe_ele)

name="sara"

rev_name =name[::-1]
if name  == rev_name:
    print("it is palindrome")
else:
    print("it is not palindrome")
