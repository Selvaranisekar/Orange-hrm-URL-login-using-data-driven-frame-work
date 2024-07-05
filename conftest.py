import pytest
from selenium import webdriver


@pytest.fixture
def browser(self):
    self.driver = webdriver.Chrome()
    yield
    self.driver.close()
