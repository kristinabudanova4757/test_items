import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin(object):


    def test_button_add_busket_presents_in_site(browser):
        link=" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        assert button.is_displayed(), "Button add to basket not displayed."