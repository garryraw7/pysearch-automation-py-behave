from behave import *
from Helpers.Browsers import Browser
from pom.pom_basic_operations import Basic
from pom.pom_homepage import Homepage
from pom.pom_webresultspage import Web


def before_all(context):
    context.basic = Basic()
    context.home_page = Homepage()
    context.web = Web()

def before_scenario(context, scenario):
    print("before scenario hook showing starting scenario name as")
    context.browser = Browser()


def after_scenario(context, scenario):
    print("after scenario hook showing ending scenario name as")
    context.browser.close()