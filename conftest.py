from selenium import webdriver
from selenium.webdriver import Chrome
import pytest
import os
from dotenv import  load_dotenv
load_dotenv()

driver = webdriver.Chrome()

@pytest.fixture(scope='class')
def setup(request):
    driver.maximize_window()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    invalid_msg_error = os.getenv("error_message_expected")
    username_loggin_in = os.getenv("USERNAME_LOGGED_IN")

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.invalid_msg_error = invalid_msg_error
    request.cls.username_loggin_in = username_loggin_in

    yield driver  # return driver
    driver.quit()


