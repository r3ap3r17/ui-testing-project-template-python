from base.base_actions import BaseActions
from data.common_strings import CommonStrings


class LoginPage(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    USERNAME_INPUT = "//input[@id='user-name']"
    PASSWORD_INPUT = "//input[@id='password']"
    SUBMIT_BUTTON = "//input[@id='login-button']"

    def verify_products_page(self):
        assert self.get_current_url() == CommonStrings.PRODUCT_PAGE_URL

    def test_successful_login(self):
        self.clear_and_type_to_element(self.USERNAME_INPUT, CommonStrings.STANDARD_USER)
        self.comment('user typed username')
        self.clear_and_type_to_element(self.PASSWORD_INPUT, CommonStrings.PASSWORD)
        self.comment('user typed password')
        self.click_element(self.SUBMIT_BUTTON)
        self.comment('user clicked submit')
        self.verify_products_page()
