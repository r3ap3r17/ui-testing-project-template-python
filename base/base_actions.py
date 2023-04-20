from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, invisibility_of_element_located, \
    presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait


class BaseActions:
    def __init__(self, driver):
        self.driver = driver
        self.count = 1

    TIMEOUT_SHORT = 5
    TIMEOUT_MEDIUM = 3
    TIMEOUT_LONG = 30



    # Console Logger
    def comment(self, log):
        print(f'\nstep 1: {log}'.upper())
        self.count += 1

    # Returns current url
    def get_current_url(self):
        return self.driver.current_url

    # Waits and returns WebElement
    def wait_for_element(self, locator, time=TIMEOUT_MEDIUM):
        wait = WebDriverWait(self.driver, timeout=time)
        return wait.until(presence_of_element_located((By.XPATH, locator)))

    # Waits for WebElement to be visible
    def wait_to_be_visible(self, locator, time=TIMEOUT_MEDIUM):
        wait = WebDriverWait(self.driver, timeout=time)
        wait.until(presence_of_element_located((By.XPATH, locator)))

    # Waits for WebElement not to be visible
    def wait_not_to_be_visible(self, locator, time=TIMEOUT_MEDIUM):
        wait = WebDriverWait(self.driver, timeout=time)
        wait.until(invisibility_of_element_located((By.XPATH, locator)))

    # Waits and returns list of WebElements
    def wait_for_elements(self, locator, time=TIMEOUT_MEDIUM):
        wait = WebDriverWait(self.driver, timeout=time)
        return wait.until(presence_of_all_elements_located((By.XPATH, locator)))

    # Clicks WebElement
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    # Types to WebElement
    def type_to_element(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    # Clears from WebElement
    def clear_from_element(self, locator):
        self.wait_for_element(locator).clear()

    # Clear and Type to WebElement
    def clear_and_type_to_element(self, locator, text):
        self.clear_from_element(locator)
        self.type_to_element(locator, text)

    # Returns text from WebElement
    def get_text_from_element(self, locator):
        return self.wait_for_element(locator).text

    # Returns attribute value from WebElement
    def get_attribute_from_element(self, locator, attr):
        return self.wait_for_element(locator).get_attribute(attr)

    # Drags and drops element
    def drag_and_drop_element(self, draggable, droppable):
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()
