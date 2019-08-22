from behave import *
# from pom.pom_basic_operations import *
# from pom.pom_webresultspage import *
# from pom.pom_homepage import *



@given(u'User loads {url} in browser')
@given(u'User opens {url} in browser')
@when(u'User loads {url} in browser')
@when(u'User opens {url} in browser')
def step_impl(context, url):
    context.basic.do_open_url(url)


@when(u'page title is "{title}"')
@then(u'page title is "{title}"')
def step_impl(context, title):
    context.basic.do_check_page_title(title)

@when(u'page URL {does_donot} contain "{search_term}"')
@then(u'page URL {does_donot} contain "{search_term}"')
def step_impl(context, does_donot, search_term):
    if does_donot == "do not":
        assert (search_term not in context.browser.driver.current_url) == True
    elif does_donot == "does":
        assert (search_term not in context.browser.driver.current_url) == False


