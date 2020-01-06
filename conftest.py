import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help="Set language")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="module")
def langopt(request):
    if request.config.getoption("--language") == 'en':
        return 'en-gb'
    else:
        return request.config.getoption("--language")


@pytest.fixture(scope="module")
def main_page_url(langopt):
    link = f"http://selenium1py.pythonanywhere.com/{langopt}/"
    return link


@pytest.fixture(scope="module")
def product_page_url(langopt):
    # link = f"http://selenium1py.pythonanywhere.com/{langopt}/catalogue/the-city-and-the-stars_95/"
    link = f'http://selenium1py.pythonanywhere.com/{langopt}/catalogue/coders-at-work_207/?promo=offer0'
    return link
