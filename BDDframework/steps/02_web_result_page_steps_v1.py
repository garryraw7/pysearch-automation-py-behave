from behave import *
from pom.pom_basic_operations import *
from pom.pom_webresultspage import *
from pom.pom_homepage import *



@when(u'User see Startpage logo is visible on Results Page')
@then(u'User see Startpage logo is visible on Results Page')
def step_impl(context):
    assert context.web.is_header_logo_available() == True

