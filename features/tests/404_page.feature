# Created by papa at 10/12/21
Feature: Tests for 404 page
  # Enter feature description here

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B07NF5WGQ11111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window
