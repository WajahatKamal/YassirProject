from seleniumpagefactory.Pagefactory import PageFactory
from service.testDataReader import userData


class LoginPage(PageFactory):
    """Define locators dictionary where key name will become WebElement using PageFactory"""
    locators = {
        "userNameField": ('XPATH', "//*[@id='user-name']"),
        "passwordField": ('XPATH', "//*[@id='password']"),
        "loginButton": ('XPATH', "//*[@id='login-button']"),
    }

    """Constructor of this class"""

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    """Page Actions for Login Page"""

    def login_username(self):
        self.userNameField.set_text(userData.userName)

    def login_password(self):
        self.passwordField.set_text(userData.password)

    def login_button(self):
        self.loginButton.click_button()

