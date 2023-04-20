import pytest
from config.config_driver import ConfigDriver


@pytest.fixture(scope='class')
def setup(request):
    # Driver setup
    driver = ConfigDriver.configure_driver()
    ConfigDriver.init_driver(driver)
    # Make driver visible to all test classes
    request.cls.driver = driver
    yield
    # Driver teardown
    ConfigDriver.close_driver(driver)
