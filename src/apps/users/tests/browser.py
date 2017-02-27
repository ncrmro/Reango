import json

from django.test import TestCase, Client, LiveServerTestCase
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.contrib.auth import get_user_model
import time


class UserTest(LiveServerTestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='test',
            last_name='user',
            email='test@user.com',
            password='top_secret'
        )
        if settings.SELENIUM_HOST:
            self.selenium = webdriver.Remote(
                command_executor=settings.SELENIUM_HOST,
                desired_capabilities=DesiredCapabilities.CHROME
            )
        else:
            self.selenium = webdriver.Firefox()
        super(UserTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(UserTest, self).tearDown()

    def test_sign_up_form(self):
        selenium = self.selenium
        selenium.implicitly_wait(10)  # seconds
        # Opening the link we want to test
        selenium.get(self.live_server_url + "/signup")
        selenium.save_screenshot('./screenshots/sign_up_page_1.png')

        # Find Fields
        email_field = selenium.find_element_by_id("textfield-Email")
        password = selenium.find_element_by_id("textfield-Password")
        password_confirmation = selenium.find_element_by_id("textfield-PasswordConfirmation")

        # Click Button to check for empty values and check
        selenium.find_element_by_xpath("//button[text()='Sign up']").click()
        selenium.save_screenshot('./screenshots/sign_up_page_2_invalid.png')
        assert 'Email isn\'t valid' in selenium.page_source
        assert 'Passwords don\'t match' in selenium.page_source

        # Fill out inputs and check for form valid
        email_field.send_keys("sign_up_test_user@test.com")
        password.send_keys("test_password")
        password_confirmation.send_keys("test_password")
        selenium.save_screenshot('./screenshots/sign_up_page_3_now_valid.png')
        assert 'Email isn\'t valid' not in selenium.page_source
        assert 'Passwords don\'t match' not in selenium.page_source
        # Click Button to check for empty values and check
        selenium.find_element_by_xpath("//button[text()='Sign up']").click()
        selenium.save_screenshot('./screenshots/sign_up_page_4_submitited.png')

        time.sleep(3)
        assert 'Email isn\'t valid' not in selenium.page_source
        assert 'Profile' in selenium.page_source
        selenium.save_screenshot('./screenshots/sign_up_page_5_redirected_to_profile.png')

    def test_login_form(self):
        selenium = self.selenium
        selenium.implicitly_wait(10)  # seconds
        # Opening the link we want to test
        selenium.get(self.live_server_url + "/login")
        selenium.save_screenshot('./screenshots/login_page_1.png')

        # Find Fields
        email_field = selenium.find_element_by_id("textfield-Email")
        password = selenium.find_element_by_id("textfield-Password")

        # Click Button to check for empty values and check
        selenium.find_element_by_xpath("//button[text()='Login']").click()
        selenium.save_screenshot('./screenshots/login_page_2_invalid.png')
        assert 'Email isn\'t valid' in selenium.page_source
        assert 'Passwords is blank' in selenium.page_source

        # Fill out inputs and check for form valid
        email_field.send_keys("test@user.com")
        password.send_keys("top_secret")
        selenium.save_screenshot('./screenshots/login_page_3_now_valid.png')
        assert 'Email isn\'t valid' not in selenium.page_source
        assert 'Passwords is blank' not in selenium.page_source

        selenium.find_element_by_xpath("//button[text()='Login']").click()
        time.sleep(3)
        assert 'Profile' in selenium.page_source
        selenium.save_screenshot('./screenshots/login_page_4_redirected_to_profile.png')



