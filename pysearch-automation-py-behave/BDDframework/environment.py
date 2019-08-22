from behave import *
from Helpers.Browsers import Browser
from pom.pom_basic_operations import Basic
from pom.pom_homepage import Homepage
from pom.pom_webresultspage import Web


def before_all(context):
    print("Before all scenario")

# Initiate all pages and browser before_scenario and teardown in after_scenario
def before_scenario(context, scenario):
    print("before scenario hook initialising browser")
    context.browser = Browser()
    context.basic = Basic(context.browser)
    context.home_page = Homepage(context.browser)
    context.web = Web(context.browser)



def after_scenario(context, scenario):
    print("after scenario hook quitting browser")
    # Below both lines are correct, can use any as per Browsers.py functions.
    # context.browser.driver.quit()
    context.browser.quit()