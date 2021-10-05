# Created by papa at 10/3/21
Feature: Amazon footer tests


  Scenario: Users can see all footer links
    Given Open Amazon page
    Then Verify 35 footer links are present
