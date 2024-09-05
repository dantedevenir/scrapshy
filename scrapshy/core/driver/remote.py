from ...components.proxy.extension import proxies
from .driver import Driver
from selenium import webdriver

class DriverRemote(Driver):
    def __init__(self, username, token, host, port, hub):
        super().__init__(username, token, host, port)
        self.driver = webdriver.Remote(
            command_executor=hub,
            options=self.options
        )