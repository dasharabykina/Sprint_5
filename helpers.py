from selenium.webdriver.support.ui import WebDriverWait
import random
from faker import Faker


def create_email():
    fake = Faker()
    return fake.email()

def create_password():
    fake = Faker()
    return fake.password(length=10)

def get_wait(driver):
    return WebDriverWait(driver, 15)

def generate_product_name():
    # Генерация случайного названия продукта
    product_name = f'Ручка {random.randint(100, 999)}'
    return product_name