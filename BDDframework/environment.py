from behave import *
from Helpers.Browsers import Browser
from pom.pom_basic_operations import Basic
from pom.pom_homepage import Homepage
from pom.pom_webresultspage import Web


def before_all(context):
    context.browser = Browser()
    context.basic = Basic()
    context.home_page = Homepage()
    context.web = Web()

def before_scenario(context, scenario):
    print("before scenario hook initialising browser")



def after_scenario(context, scenario):
    print("after scenario hook quitting browser")
    context.browser.driver.quit()