import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    #service =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.get(r"https://demo.automationtesting.in/FileUpload.html")
    driver.maximize_window()
    yield driver                    # 🔹 Test runs at this point
    driver.quit()