# Created by papa at 10/3/21
Feature: Amazon Prime tests
  # Enter feature description here

  Scenario: Verify user sees correct amount of benefit boxes
    Given Open Amazon Prime
    Then Verify 3 benefit boxes are present
