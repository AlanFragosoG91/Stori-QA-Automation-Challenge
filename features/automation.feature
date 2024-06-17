Feature: Stori-QA-Automation-Challenge

  Scenario: Suggestion Class Example
    Given I open the browser and navigate to the automation practice page
    When I enter "Me" and select "Mexico"
    And I enter "Uni" and select "United States (USA)"
    And I enter "Uni" and select "United Arab Emirates"
    Then I close the browser

  Scenario: Dropdown Example
    Given I open the browser and navigate to the automation practice page
    When I select option 2 in the dropdown
    And I select option 3 in the dropdown
    Then I close the browser

  Scenario: Switch Window Example
    Given I open the browser and navigate to the automation practice page
    When I click the Open Window button
    Then I verify the 30 day money back guarantee text
    And I close the new window

  Scenario: Switch Tab Example
    Given I open the browser and navigate to the automation practice page
    When I click the Open Tab button
    Then I scroll to the specific button and take a screenshot
    And I return to the original tab

  Scenario: Switch To Alert Example
    Given I open the browser and navigate to the automation practice page
    When I type "Stori Card" and click the Alert button
    Then I verify and accept the alert text
    And I type "Stori Card" and click the Confirm button
    And I verify and accept the confirm text

  Scenario: Web Table Example
    Given I open the browser and navigate to the Web Table Example
    Then I print the courses that cost $25
    And I print the courses that cost $15

  Scenario: Web Table Fixed Header Example
    Given I open the browser and navigate to the automation practice page
    Then I print the names of all Engineers
    And I print the names of all Businessmans

  Scenario: iFrame Example
    Given I open the browser and navigate to the automation practice page
    Then I print the text highlighted in blue