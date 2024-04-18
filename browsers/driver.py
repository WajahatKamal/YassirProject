from selenium import webdriver
from accessconfig import settings


class Driver(object):
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    def __init__(self):
        if settings.browser == "chrome":
            self.driver = webdriver.Chrome(
                executable_path="C:\\Users\\wajahat.kamal\\PycharmProjects\\Yassir Test "
                                "Project\\browsers\\chromedriver.exe")
        else:
            raise Driver.SeleniumDriverNotFound(
                {settings.browser} + " is not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def close_browser(self):
        self.driver.close()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver()
