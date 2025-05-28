import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait_time = wait_time

    @allure.step('Wait until the element is displayed: {locator}.')
    def wait_element_is_visible(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located(locator))

    @allure.step('Fill the input field {locator} with value: {text}.')
    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Find element: {locator}.')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Collect the list of elements.')
    def collect_list_of_elements(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Get text of the element: {locator}.')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Click on element: {locator}.')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Get the field attribute.')
    def get_field_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Wait until the element is clickable: {locator}.')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable(locator))

    @allure.step('Click on element: {locator}.')
    def click_on_element_as_virtual_mouse(self, locator):
        action = ActionChains(self.driver)
        self.wait_element_is_clickable(locator)
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Scroll to the element: {locator}.')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Hover over element: {locator}.')
    def hover_element(self, locator):
        action = ActionChains(self.driver)
        self.wait_element_is_visible(locator)
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()

    @allure.step('Wait until the element is not displayed on the page: {locator}.')
    def wait_element_is_not_displayed(self, locator):
        return WebDriverWait(self.driver, timeout=60).until(EC.invisibility_of_element_located(locator))
