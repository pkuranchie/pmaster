# Created by papa at 9/21/21
Feature: test cases for search functionality
  # Enter feature description here

  Scenario Outline: User can search for a product on Amazon
    Given Open Amazon page
    When Input <search_word> into amazon search
    When Click on amazon search icon
    Then Verify <result> text is shown
    Examples:
    |search_word     |result  |
    |table           |"table" |
    |mug             |"mug"   |

