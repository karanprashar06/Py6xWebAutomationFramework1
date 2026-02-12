import pytest
import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from dotenv import load_dotenv
import os
from src.test.utils.Utils import *



@allure.title("VWO negative case")
@allure.description("TC#1 VWO negative case")
@allure.feature("VWO Login with negative credentials")
@pytest.mark.negative_case
def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=chrome_options)

    driver.get(os.getenv("URL"))

    take_screen_shot(driver=driver, name="vwo_login_step1")

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(3)

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)

    take_screen_shot(driver=driver, name="vwo_login_step2")
    assert error_message_web_element.text == os.getenv("error_message_expected")

    time.sleep(3)
    driver.quit()