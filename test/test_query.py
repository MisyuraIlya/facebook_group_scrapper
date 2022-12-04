import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.ui  import WebDriverWait

@pytest.mark.usefixtures('setup')
class TestQuery:

    def test_query(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(0.5)
        element1 = driver.find_element(By.CSS_SELECTOR, '#')

        wait = WebDriverWait(driver, 15, 0.3)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#')))
