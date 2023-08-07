import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    USERNAME_SELECTOR = (By.ID, 'username')
    PASSWORD_SELECTOR = (By.ID, 'password')
    LOGIN_SELECTOR = (By.XPATH, '//button')
    ERROR_SELECTOR = (By.ID, 'flash')
    LOGOUT_SELECTOR = (By.CSS_SELECTOR, 'i[class="icon-2x icon-signout"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get('https://the-internet.herokuapp.com/login')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_wrong_username(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys('Mihai')
        #time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('SuperSecretPassword!')
        #time.sleep(2)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #time.sleep(2)
        assert self.driver.find_element(*self.ERROR_SELECTOR).text == 'Your username is invalid!\n×'

    def test_login_wrong_password(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys('tomsmith')
        #time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('1234')
        #time.sleep(2)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #time.sleep(2)
        assert self.driver.find_element(*self.ERROR_SELECTOR).text == 'Your password is invalid!\n×'

    def test_login_empty_username_and_password(self):
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #time.sleep(2)
        assert self.driver.find_element(*self.ERROR_SELECTOR).text == 'Your username is invalid!\n×'

    def test_correct_login(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys('tomsmith')
        #time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('SuperSecretPassword!')
        #time.sleep(2)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #time.sleep(2)
        assert self.driver.find_element(*self.ERROR_SELECTOR).text == 'You logged into a secure area!\n×'

    def test_logout(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys('tomsmith')
        #time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('SuperSecretPassword!')
        #time.sleep(2)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #time.sleep(2)
        self.assertEqual(self.driver.find_element(*self.ERROR_SELECTOR).text, 'You logged into a secure area!\n×')
        self.driver.find_element(*self.LOGOUT_SELECTOR).click()
        #time.sleep(2)
        self.assertEqual(self.driver.find_element(*self.ERROR_SELECTOR).text, 'You logged out of the secure area!\n×', 'Logout error')





