# Created by papa at 9/29/21
Feature: test cases for Homework 2
  # Enter feature description here

  Scenario: User getting help with cancel orders
    Given Open Amazon help page
    When Input Cancel Order into search field
    Then Verify Cancel Items or Orders text is shown


