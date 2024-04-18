from pytest_bdd import scenario, given, parsers, when, then
from browsers import driver
from service.pages.loginPage import LoginPage
from service.pages.homePage import HomePage


@given("User Setups the Web Browser")
def userSetupTheWebBrowser():
    print("Passed")


@given(parsers.cfparse('User Navigates to "{urlToLoad}" Url'))
def userNavigateToUrl(urlToLoad):
    webdriver = driver.driver.get_driver()
    webdriver.maximize_window()
    webdriver.get("https://www.saucedemo.com/")
    print("URL", urlToLoad)


@when('User Enters "valid.username" on UserName Field on Login Page')
def user_name():
    webdriver = driver.driver.get_driver()
    pglogin = LoginPage(webdriver)
    pglogin.login_username()


@when('User Enters "valid.password" on Password Field on Login Page')
def user_passwrd():
    webdriver = driver.driver.get_driver()
    pglogin = LoginPage(webdriver)
    pglogin.login_password()


@when('User Clicks on Login Button on Login Page')
def user_login_button():
    webdriver = driver.driver.get_driver()
    pglogin = LoginPage(webdriver)
    pglogin.login_button()


@scenario(
    'C:\\Users\\wajahat.kamal\\PycharmProjects\\Yassir Test Project\\service\\tests\\features\\first_scenario.feature',
    'Verify that the User lands on the homepage successfully')
def test_company_module():
    print("Test Successful!!!!!!!")


@given("User Successfully Logged in test Application")
def userSuccessfullyLandsOnURL():
    print("Passed")


@then("User should see the Products page")
def userShouldSeeProductPage():
    webdriver = driver.driver.get_driver()
    pghome = HomePage(webdriver)
    pghome.title_homepage()


@then("User should scroll down the page")
def userShouldScrollDown():
    webdriver = driver.driver.get_driver()
    pghome = HomePage(webdriver)
    pghome.scroll_homepage()


@then("User adds an item in the cart")
def userAddsIteminCart():
    webdriver = driver.driver.get_driver()
    pghome = HomePage(webdriver)
    pghome.add_item()

@then("User confirms that the filter is working")
def userConfrimFilter():
    webdriver = driver.driver.get_driver()
    pghome = HomePage(webdriver)
    pghome.page_filter()