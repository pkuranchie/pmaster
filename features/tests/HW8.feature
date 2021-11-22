# Created by papa at 11/22/21
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias computers
    And Input Dell into amazon search
    And Click on amazon search icon
    Then Verify pc department is selected

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals option
    Then Verify deals are present