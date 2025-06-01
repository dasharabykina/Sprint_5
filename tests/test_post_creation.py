from locators import *
from urls import *
from conftest import *
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from data import advertisement


class TestPostCreation:
    def test_create_ad_unauthenticated_user_error(self, driver, open_main_page):
        wait = get_wait(driver)
        driver.find_element(*BUTTON_CREATE_AD).click()
        assert driver.find_element(*NOTIFICATION_MODAL).is_displayed()


    def test_create_ad_authenticated_user_success(self, driver, open_main_page, login):
        wait = get_wait(driver)
        product = generate_product_name()
        
        wait.until(EC.presence_of_element_located((BUTTON_CREATE_AD)))
        wait.until(EC.element_to_be_clickable(BUTTON_CREATE_AD)).click()
        
        driver.find_element(*INPUT_TITLE).send_keys(product)
        driver.find_element(*INPUT_DESCRIPTION).send_keys(advertisement.description)
        driver.find_element(*INPUT_PRICE).send_keys(advertisement.price)
        
        driver.find_element(*DROPDOWN_CATEGORY).click()
        wait.until(EC.element_to_be_clickable(SELECT_CATEGORY)).click()

        driver.find_element(*DROPDOWN_CITY).click()
        wait.until(EC.element_to_be_clickable(SELECT_CITY)).click()

        driver.find_element(*RADIO_CONDITION).click()
        wait.until(EC.element_to_be_clickable(BUTTON_PUBLISH)).click()

        driver.execute_script("window.scrollTo(0, 0);")
        wait.until(EC.element_to_be_clickable(AVATAR_BUTTON)).click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located(SECTION_MY_ADS))

        assert wait.until(EC.visibility_of_element_located(ITEM_AD)).is_displayed()