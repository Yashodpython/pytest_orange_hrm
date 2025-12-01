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

switch_to_windows_xpath="//div[@class='navbar-collapse collapse navbar-right']/child::ul/li[4]/ul/li[2]/a"
switch_to_windows_element=wait.until(EC.presence_of_element_located((By.XPATH,switch_to_windows_xpath)))
switch_to_windows_element.click()

#click button to open new tab

click_button_xpath="//div[@id='Tabbed']/descendant::a"
click_button_element=wait.until(
    EC.element_to_be_clickable((By.XPATH,click_button_xpath))
)

click_button_element.click()

windows=driver.window_handles
driver.switch_to.window(windows[1])

selenium_link_xpath="//a[@class='navbar-brand']"
selenium_link_element=driver.find_element(By.XPATH,selenium_link_xpath)
if selenium_link_element.is_displayed():
    print("switched to new window and finded selenium link xpath")
    span_element=driver.find_element(By.XPATH,"//a[@class='navbar-brand']/span")
    if span_element.is_displayed():
        print(span_element.get_attribute("class"))
else:
    print("the finding eleement is not displayed")


time.sleep(10)