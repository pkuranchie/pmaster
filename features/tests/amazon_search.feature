# Created by papa at 9/21/21
Feature: test cases for search functionality
  # Enter feature description here

#  Scenario: User can see language options
#    Given Open Amazon page
#    When Hover over language options
#    Then Verify correct options present

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias stripbooks
    And Input Faust into amazon search
    And Click on amazon search icon
    Then Verify books department is selected

