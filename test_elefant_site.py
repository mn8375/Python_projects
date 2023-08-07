import time
import unittest

from selenium import webdriver
from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By

class TestElefant(unittest.TestCase):
    COOKIE_BUTTON = (By.CSS_SELECTOR,"button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.close")
    MOBILE_LOGO = (By.CSS_SELECTOR, "a.mobile-logo")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(4)
        self.driver.implicitly_wait(3)
        self.driver.get('https://www.elefant.ro/')
        try:
            self.driver.find_element(*self.COOKIE_BUTTON).click()
        except NoSuchElementException:
            pass

        self.driver.maximize_window()
        time.sleep(4)

    def tearDown(self) -> None:
        # time.sleep(1)
        self.driver.quit()

    def test_elefant_site(self):

        try:
            self.driver.find_element(*self.CLOSE_BUTTON).click()
        except ElementNotInteractableException:
            pass
        try:
            self.driver.find_element(*self.MOBILE_LOGO)

        except NoSuchElementException:
            assert False, "Elementul nu a fost gasit."


    def test_search_bar(self):
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Căutați cuvânt cheie, codul de produs, tip produs"]').send_keys("Carti")
        self.driver.find_element(By.XPATH, '//button[@name = "search"]').click()
        #[class="product-title"]
        items_list = self.driver.find_elements(By.CSS_SELECTOR,'[class="product-title"]')
        time.sleep(2)
        assert len(items_list) >= 5, f'Lungimea listei este de {len(items_list)}'


    def test_title(self):

        assert self.driver.title =='elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!'


        #//span[contains(text(),"Cont")]
    def test_login_wrong_credentials(self):
        self.driver.find_element(By.XPATH, '//span[text()="Cont"]').click()

        #a.my-account-login
        self.driver.find_element(By.CSS_SELECTOR, "a.my-account-login").click()
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Email"]').send_keys('abc22@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Parola"]').send_keys('12345')

        self.driver.find_element(By.NAME, "login").click()

        mesaj = self.driver.find_element(By.CSS_SELECTOR, '[role="alert"]').text
        assert mesaj == "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."




