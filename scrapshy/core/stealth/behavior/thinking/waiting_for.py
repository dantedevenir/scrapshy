from ..keyboard.push import Keyboard
from ..mouse.move import Mouse
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from policy.models.healthcare import xpath

class WaitingFor:
    def __init__(self, driver):
        self.driver = driver
        self.keyboard = Keyboard(driver)
        self.mouse = Mouse(driver)
    def Key(self, key):
        keyUpper = str(key).upper()
        if keyUpper ==  "ENTER":
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def Elements(self, selector, reference):
            Passes = 0
            current_url =self.driver.current_url
            wait = WebDriverWait(self.driver, 5)
            while True and Passes < 10:
                elem_wait =self.driver.find_elements(selector, reference)
                try:
                    wait.until(EC.presence_of_element_located((selector, reference)))
                    if len(elem_wait) == 0:
                        Passes += 2
                    else:
                        Passes = 10
                except TimeoutException:
                    print("TimeoutException")
                    if EC.presence_of_element_located((selector, reference)):
                        Passes = 10
                    elif Passes >= 6:
                       self.driver.refresh()
                Passes += 3
            return elem_wait

    def Element(self, selector, reference, action = None, word = None):
        Passes = 0
        current_url =self.driver.current_url
        Actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver,10)
        timeOut = 0
        while True and Passes < 10:
            print("Waiting for ",reference)
            try:
                wait.until(EC.presence_of_element_located((selector, reference)))
                elem_wait =self.driver.find_element(selector, reference)           
                if action:
                    Actions.move_to_element(elem_wait)
                    Actions.click(elem_wait).perform()
                    if action == "goto":
                        wait.until(EC.url_changes(current_url))
                        current_url =self.driver.current_url
                    elif action == "hold":
                        wait.until(EC.element_to_be_clickable((selector, reference)))
                    elif action == "flex":
                        wait.until(EC.presence_of_element_located((selector, reference)))
                if word:
                    By.XPATH
                    for letter in word:
                        ActionChains(self.driver).send_keys(letter).perform()
                        ActionChains(self.driver).pause(0.8).perform()
                        ActionChains(self.driver).reset_actions()
                Passes += 10
            except NoSuchElementException:
                print("NoSuchElementException")
                Passes += 5
            except TimeoutException:
                print("TimeoutException")
                if reference == xpath.SubmitReset:
                    pass
                elif reference == xpath.ReportLifeChangesModal_ContinueButton:
                    print(self.driver.current_url)
                    print(current_url)
                    self.driver.back()
                elif reference == xpath.Continue:
                    print(self.driver.current_url)
                    print(current_url)
                    self.driver.back()
                Passes += 3
                timeOut += 1
                if Passes >= 6:
                    if reference == xpath.Status:
                        raise NoSuchElementException
                    elif reference == xpath.ReportLifeChangesModal_ContinueButton:
                        Passes = 10
                    if word == "ReportLifeChange":
                       self.driver.back()
                    self.driver.refresh()
            except StaleElementReferenceException:
                elem_wait =self.driver.find_element(selector, reference)
                Passes += 5
            except IndexError:
                Passes += 5
                self.driver.refresh()
            Actions.reset_actions()

        if timeOut == 4:
            campaign = "TimeOut"
            """self.history('NULL'.encode(), 'NULL'.encode(),'NULL'.encode(), 'NULL'.encode(), 'NULL'.encode(), campaign.encode())"""
            raise WebDriverException