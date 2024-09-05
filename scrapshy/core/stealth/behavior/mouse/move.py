from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Mouse:  
    def __init__(self, driver):
        self.driver = driver
    def move(self, selector, reference, Passes, action = None):
        Passes = Passes
        current_url = self.driver.current_url
        Actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 10)
        while True and Passes < 10:
            print("Waiting for ",reference)
            try:
                wait.until(EC.presence_of_element_located((selector, reference)))
                elem_wait = self.driver.find_element(selector, reference)           
                Actions.move_to_element(elem_wait)
                Actions.click(elem_wait).perform()
                if action == "goto":
                    wait.until(EC.url_changes(current_url))
                    current_url = self.driver.current_url
                elif action == "hold":
                    wait.until(EC.element_to_be_clickable((selector, reference)))
                elif action == "flex":
                    wait.until(EC.presence_of_element_located((selector, reference)))
                Passes += 10
            except NoSuchElementException:
                print("NoSuchElementException")
                Passes += 5

            Actions.reset_actions()