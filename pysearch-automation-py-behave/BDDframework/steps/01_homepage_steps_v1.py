from behave import *
# from pom.pom_basic_operations import *
# from pom.pom_webresultspage import *
# from pom.pom_homepage import *


@given(u'User search "{search_term}" on homepage')
@when(u'User search "{search_term}" on homepage')
def step_impl(context, search_term):
    context.home_page.do_perform_search_homepage(search_term)
