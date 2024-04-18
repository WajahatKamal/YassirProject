import time
from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    """Define locators dictionary where key name will become WebElement using PageFactory"""
    locators = {
        "homepageAssertion": ('XPATH', "//*[@id='header_container']/div[2]/span"),
        "addtocart": ('XPATH', "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button"),
        "priceforfirstitem": ('XPATH', "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div"),
        "filterhomepage": ('XPATH', "//*[@id='header_container']/div[2]/div/span/select"),
        "filterhomepageselection": ('XPATH', "//*[@id='header_container']/div[2]/div/span/select/option[3]")
    }

    """Constructor of this class"""

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    """Page Actions for Login Page"""

    def title_homepage(self):
        element = self.homepageAssertion.text
        assert element == 'Products'

    """Scroll down the web page"""

    def scroll_homepage(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 250)")

    """Adding an item in the cart and confirming if the item has been added or not"""

    def add_item(self):
        time.sleep(5)
        self.addtocart.click_button()
        element = self.addtocart.text
        print(element)
        assert element == 'Remove'

    """Changing the filter and confirming if the change made is working fine or not"""

    def page_filter(self):
        element1 = self.priceforfirstitem.text
        self.filterhomepage.click()
        time.sleep(2)
        self.filterhomepageselection.click()
        element2 = self.priceforfirstitem.text
        assert element2 != element1
