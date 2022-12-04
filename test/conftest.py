import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # use headless if yout not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1640,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver
    # driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver', options=options)
    # path to the web driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://www.facebook.com/groups/265893208051540/?ref=share&mibextid=S66gvF"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()