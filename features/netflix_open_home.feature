Feature: Netflix Launch

  Scenario: Open Netflix and return Home

    Given TV is on Home screen

    When user presses Netflix button

    Then Netflix should open

    When user presses Home button

    Then TV should return to Home screen