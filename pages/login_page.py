import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager





def open_browser():
    global driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.get(r"https://demo.automationtesting.in/FileUpload.html")
    driver.maximize_window()
    time.sleep(5)

def enter_username(username):

    username_xpath="//input[@name='username']"
    driver.find_element(By.XPATH, username_xpath).send_keys(username)
def enter_password(password):
    password_xpath="//input[@name='password']"
    driver.find_element(By.XPATH, password_xpath).send_keys(password)
def click_on_login_button():
    driver.find_element(By.XPATH,"//div[@class='oxd-form-actions orangehrm-login-action']/button").click()
    time.sleep(10)

def assert_login_page():

    Dash_board_xapth="//h6[text()='Dashboard']"
    dashboard_text=driver.find_element(
        By.XPATH, Dash_board_xapth
    ).text

    assert dashboard_text == "Dashboard","it is not matched"

def assert_in_valid_login_page():
    invalid_pop_up_msg_xpath="//div[@class='oxd-alert oxd-alert--error']//p"
    invalid_msg=driver.find_element(By.XPATH, invalid_pop_up_msg_xpath).text
    assert "inv" in invalid_msg.lower() , "it is not matched"
def close_browser():
    driver.quit()