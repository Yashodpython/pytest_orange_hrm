import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    service = Service(r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")   # 🔹 Open browser
    driver.maximize_window()
    yield driver                    # 🔹 Test runs at this point
    driver.quit()