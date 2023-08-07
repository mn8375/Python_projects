import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestAlerts(unittest.TestCase):
    JS_ALERT_SELECTOR = (By.CSS_SELECTOR, 'button[onclick = "jsAlert()"]')
    MESSAGE_SELECTOR = (By.ID, 'result')
    CONFIRM_SELECTOR = (By.CSS_SELECTOR, 'button[onclick = "jsConfirm()"]')
    PROMPT_SELECTOR = (By.CSS_SELECTOR, 'button[onclick = "jsPrompt()"]')
    CONTEXT_SELECTOR = (By.ID, 'hot-spot')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_js_alert(self):
        self.driver.find_element(*self.JS_ALERT_SELECTOR).click()
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(*self.MESSAGE_SELECTOR).text == 'You successfully clicked an alert'

    def test_js_cancel(self):
        self.driver.find_element(*self.CONFIRM_SELECTOR).click()
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(*self.MESSAGE_SELECTOR).text == 'You clicked: Cancel'

    def test_js_prompt(self):
        self.driver.find_element(*self.PROMPT_SELECTOR).click()
        text = 'Asa trebuie sa ruleze pagina'
        self.driver.switch_to.alert.send_keys(text)
        self.driver.switch_to.alert.accept()
        self.assertEqual(self.driver.find_element(*self.MESSAGE_SELECTOR).text, f'You entered: {text}')

    def test_alert_from_contextmenu(self):
        self.driver.get('https://the-internet.herokuapp.com/context_menu')
        ac = ActionChains(self.driver)
        element = self.driver.find_element(*self.CONTEXT_SELECTOR)
        ac.context_click(element).perform()
        self.driver.switch_to.alert.accept()


