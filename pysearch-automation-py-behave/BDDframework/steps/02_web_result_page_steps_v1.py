from behave import *
from pom.pom_basic_operations import *



@given(u'User loads {url} in browser')
@given(u'User opens {url} in browser')
@when(u'User loads {url} in browser')
@when(u'User opens {url} in browser')
def step_impl(context, url):
    context.basic.do_open_url(url)


@given(u'User search "{search_term}" on homepage')
@when(u'User search "{search_term}" on homepage')
def step_impl(context, search_term):
    context.home_page.do_perform_search_homepage(search_term)


@then(u'page title is "{title}"')
def step_impl(context, title):
    context.basic.do_check_page_title(title)

