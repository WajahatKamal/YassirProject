Feature: Test URL Feature File
  Contains test cases for the current project

  Background:
    Given User Setups the Web Browser
    And User Navigates to "test.url" Url
    When User Enters "valid.username" on UserName Field on Login Page
    And User Enters "valid.password" on Password Field on Login Page
    And User Clicks on Login Button on Login Page


  Scenario: Verify that the User lands on the homepage successfully

    Given User Successfully Logged in test Application
    Then User should see the Products page
    And User should scroll down the page
    Then User adds an item in the cart
    And User confirms that the filter is working
