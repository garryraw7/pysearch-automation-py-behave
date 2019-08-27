@webpage @all
Feature: Pysearch Web Results page verification



  @title
  Scenario: Verify the page title on the Web Result page.
    Given User loads https://www.startpage.com in browser
    When User search "tesla" on homepage
    Then page title is "Startpage.com Search results"


  @title
  Scenario Outline: Verify that the default search technique do not expose search term in URL
    #Sometimes a scenario should be run with a number of variables giving a set of known states, actions to take and expected outcomes, all using the same basic actions.
  # You may use a Scenario Outline like below to achieve this#
    Given User loads https://www.startpage.com in browser
    When User search "<search_term>" on homepage
    Then page URL do not contain <search_term>

    Examples: Test Data
          | search_term	|
          | tiger 		|
          | jfk			|


    @navigation
    Scenario: Verify that the Header bar shows Startpage logo
      Given User loads https://www.startpage.com in browser
      And User search "tesla" on homepage
#      Then User see Startpage logo is visible on Results Page