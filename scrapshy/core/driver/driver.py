from ...components.proxy.extension import proxies
from selenium import webdriver

class Driver():
    def __init__(self, username, token, host, port):
        proxies_extension = proxies(username, token, host, port)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-infobars")
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("log-level=3")
        self.options.add_extension(proxies_extension)