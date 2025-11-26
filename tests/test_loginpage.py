import sys
sys.path.append(r"C:\Users\Admin\Desktop\Python_Practise")

from pages.login_page import *


def test_validate_loginpage_with_valid_credentials():
    open_browser()
    enter_username("Admin")
    enter_password("admin123")
    click_on_login_button()
    assert_login_page()
    close_browser()

def test_validate_loginpage_with_invalid_credentials():
    open_browser()
    enter_username("rete")
    enter_password("admin123")
    click_on_login_button()
    assert_in_valid_login_page()
    close_browser()

def test_validate_loginpage_with_valid1_credentials():
    open_browser()
    enter_username("Admin")
    enter_password("admin123")
    click_on_login_button()
    assert_login_page()
    close_browser()

def test_validate_loginpage_with_invalid1_credentials():
    open_browser()
    enter_username("rete")
    enter_password("admin123")
    click_on_login_button()
    assert_in_valid_login_page()
    close_browser()





