import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestSuccessfulLogin:
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.test_successful_login()
