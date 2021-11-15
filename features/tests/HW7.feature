# Created by papa at 10/13/21
Feature: Seeing Sign in page after logging out
  # Enter feature description here

  Scenario: Add a product to the cart
    Given Open Amazon page
    When Input Dress into amazon search
    And Click on amazon search icon
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product


