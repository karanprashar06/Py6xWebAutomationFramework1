import allure
import pytest
from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.pageObjects.PF.loginPage_PageFactory import LoginPage
from src.test.pageObjects.PF.dashboard_PageFactory import DashboardPage
from dotenv import load_dotenv
import os
from src.test.utils.Utils import *
import logging


@allure.epic("VWO App login Check!")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants().app_url())
            loginPage = LoginPage(driver)
            # loginPage.login_to_vwo(usr=self.username, pwd="123")
            loginPage.login_to_vwo(usr="admin@vwo.com", pwd="123")
            error_msg_text = loginPage.error_msg()
            assert error_msg_text == self.invalid_msg_error

        except Exception as e:
            print(e)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_positive(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants().app_url())
            loginPage = LoginPage(driver=driver)
            LOGGER.info("Login is done!")
            loginPage.login_to_vwo(usr=self.username, pwd=self.password)
            dashboardPage = DashboardPage(driver=driver)
            LOGGER.info("Dashboard loaded!")
            username_logging = dashboardPage.user_logged_in_text()
            print(username_logging)
            assert self.username_loggin_in == username_logging

        except Exception as e:
            print(e)
