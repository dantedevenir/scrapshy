from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Keyboard:
    def __init__(self, driver):
        self.driver = driver
    def push(self, selector, reference, Passes, letter):
        Passes = Passes
        current_url = self.driver.current_url
        Actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 10)
        while True and Passes < 10:
            print("Waiting for ",reference)
            try:
                wait.until(EC.presence_of_element_located((selector, reference)))
                elem_wait = self.driver.find_element(selector, reference)           
                By.XPATH
                ActionChains(self.driver).send_keys(letter).perform()
                ActionChains(self.driver).pause(0.8).perform()
                ActionChains(self.driver).reset_actions()
                Passes += 10
            except NoSuchElementException:
                print("NoSuchElementException")
                Passes += 5

            Actions.reset_actions()