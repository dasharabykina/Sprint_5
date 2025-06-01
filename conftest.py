import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import *
from selenium.webdriver.support import expected_conditions as EC
from urls import *
from data import Login_Exist_User
from helpers import *


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(options = options)
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(driver):
    driver.get(BASE_URL)

@pytest.fixture
def login(driver, open_main_page):
    wait = get_wait(driver)
    wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(Login_Exist_User.exist_user_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
    driver.find_element(*LOGIN_BUTTON).click()
