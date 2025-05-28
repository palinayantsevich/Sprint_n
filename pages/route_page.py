import allure

from pages.base_page import BasePage
from locators import RoutePageLocators
from data import RoutePageData

from selenium.common.exceptions import TimeoutException, NoSuchElementException


class RoutePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RoutePageLocators()

    @allure.step('Fill in the "From" field: "{address}".')
    def wait_fill_from_field(self, address):
        self.wait_element_is_visible(self.locators.FROM_FIELD)
        self.fill_input(self.locators.FROM_FIELD, address)

    @allure.step('Fill in the "Where" field: "{address}".')
    def wait_fill_where_field(self, address):
        self.wait_element_is_visible(self.locators.TO_FIELD)
        self.fill_input(self.locators.TO_FIELD, address)

    @allure.step('Fill in the "From" and "Where" field: from "{from_address}" to "{where_address}".')
    def wait_fill_from_and_where_fields(self, from_address, where_address):
        self.wait_element_is_visible(self.locators.FROM_FIELD)
        self.fill_input(self.locators.FROM_FIELD, from_address)
        self.wait_element_is_visible(self.locators.TO_FIELD)
        self.fill_input(self.locators.TO_FIELD, where_address)

    @allure.step('Check the placeholder text in the "FROM" field.')
    def check_from_field_placeholder_text(self):
        self.wait_element_is_visible(self.locators.FROM_FIELD_PLACEHOLDER)
        return self.get_element_text(self.locators.FROM_FIELD_PLACEHOLDER)

    @allure.step('Check the placeholder text in the "TO" field.')
    def check_to_field_placeholder_text(self):
        self.wait_element_is_visible(self.locators.TO_FIELD_PLACEHOLDER)
        return self.get_element_text(self.locators.TO_FIELD_PLACEHOLDER)

    @allure.step('Find A (from) and B (where) points on the map.')
    def find_ab_points_on_map(self):
        return self.collect_list_of_elements(self.locators.AB_POINTS_ROUTE)

    @allure.step('Check that the route section is displayed.')
    def check_route_section_displayed(self):
        if self.wait_element_is_visible(self.locators.ROUTE_SECTION):
            return True
        else:
            return False

    @allure.step('Check the text in the route section.')
    def check_route_section_price_text(self):
        self.wait_element_is_visible(self.locators.ROUTE_SECTION_TEXT)
        return self.get_element_text(self.locators.ROUTE_SECTION_TEXT)

    @allure.step('Check the duration text in the route section.')
    def check_route_section_duration_text(self):
        self.wait_element_is_visible(self.locators.ROUTE_SECTION_DURATION)
        return self.get_element_text(self.locators.ROUTE_SECTION_DURATION)

    @allure.step('Check the price value in the route section.')
    def check_route_section_price_value(self):
        self.wait_element_is_visible(self.locators.ROUTE_SECTION_TEXT)
        price_with_text = self.get_element_text(self.locators.ROUTE_SECTION_TEXT)
        price_value = ''.join(filter(str.isdigit, price_with_text))
        return price_value

    @allure.step('Check the duration value in the route section.')
    def check_route_section_duration_value(self):
        self.wait_element_is_visible(self.locators.ROUTE_SECTION_DURATION)
        duration_with_text = self.get_element_text(self.locators.ROUTE_SECTION_DURATION)
        duration_value = ''.join(filter(str.isdigit, duration_with_text))
        return duration_value

    @allure.step('Click on the "Optimal" tab in the route section.')
    def wait_click_on_optimal_tab(self):
        self.wait_element_is_visible(self.locators.OPTIMAL_ROUTE_TAB)
        self.click_on_element(self.locators.OPTIMAL_ROUTE_TAB)

    @allure.step('Check if the "Optimal" tab is active.')
    def check_optimal_tab_is_active(self):
        return self.get_field_attribute(self.locators.OPTIMAL_ROUTE_TAB, RoutePageData.ACTIVE_TAB_ATTRIBUTE)

    @allure.step('Click on the "Fast" tab in the route section.')
    def wait_click_on_fast_tab(self):
        self.wait_element_is_visible(self.locators.FAST_ROUTE_TAB)
        self.click_on_element(self.locators.FAST_ROUTE_TAB)

    @allure.step('Check if the "Fast" tab is active.')
    def check_fast_tab_is_active(self):
        return self.get_field_attribute(self.locators.FAST_ROUTE_TAB, RoutePageData.ACTIVE_TAB_ATTRIBUTE)

    @allure.step('Click on the "Personal" tab in the route section.')
    def wait_click_on_personal_tab(self):
        self.wait_element_is_visible(self.locators.PERSONAL_ROUTE_TAB)
        self.click_on_element(self.locators.PERSONAL_ROUTE_TAB)

    @allure.step('Check if the "Personal" tab is active.')
    def check_personal_tab_is_active(self):
        return self.get_field_attribute(self.locators.PERSONAL_ROUTE_TAB, RoutePageData.ACTIVE_TAB_ATTRIBUTE)

    @allure.step('Check the state of the movement type.')
    def check_movement_type_state(self, movement_type):
        return self.get_field_attribute(self.locators.build_movement_type_locator(movement_type),
                                        RoutePageData.MOVEMENT_TYPE_ATTRIBUTE)

    @allure.step('Click on the "Get TAXI" button.')
    def wait_click_on_get_taxi_button(self):
        self.wait_element_is_clickable(self.locators.GET_TAXI_BUTTON)
        self.click_on_element(self.locators.GET_TAXI_BUTTON)

    @allure.step('Verify that tariff selection section is displayed.')
    def check_taxi_tariff_section_displayed(self):
        if self.wait_element_is_visible(self.locators.TARIFF_PICKER_SECTION):
            return True
        else:
            return False

    @allure.step('Click on "Drive" movement type icon.')
    def wait_click_on_drive_movement_icon(self):
        self.wait_element_is_visible(self.locators.AB_POINTS_ROUTE)
        self.wait_element_is_clickable(self.locators.DRIVE_MOVEMENT_TYPE)
        self.click_on_element_as_virtual_mouse(self.locators.DRIVE_MOVEMENT_TYPE)

    @allure.step('Click on the "Book" button.')
    def wait_click_on_book_button(self):
        self.wait_element_is_clickable(self.locators.BOOK_BUTTON)
        self.click_on_element_as_virtual_mouse(self.locators.BOOK_BUTTON)

    @allure.step('Verify that specific taxi tariff is displayed.')
    def wait_check_taxi_tariff_displayed(self, taxi_tariff):
        self.wait_element_is_visible(self.locators.TARIFF_PICKER_SECTION)
        if self.wait_element_is_visible(self.locators.build_taxi_tariff_card_locator(taxi_tariff)):
            return True
        else:
            return False

    @allure.step('Check active taxi tariff.')
    def find_active_taxi_tariffs(self):
        return self.collect_list_of_elements(self.locators.ACTIVE_TAXI_TARIFF)

    @allure.step('Click on taxi tariff.')
    def wait_click_on_taxi_tariff(self, taxi_tariff):
        self.wait_element_is_visible(self.locators.build_taxi_tariff_card_locator(taxi_tariff))
        self.click_on_element(self.locators.build_taxi_tariff_card_locator(taxi_tariff))

    @allure.step('Hover over taxi tariff tooltip icon.')
    def wait_hover_taxi_tariff_tooltip(self, taxi_tariff_number):
        try:
            self.wait_element_is_visible(self.locators.AB_POINTS_ROUTE)
            self.wait_element_is_visible(self.locators.build_taxi_tariff_tooltip_icon_locator(taxi_tariff_number))
            self.hover_element(self.locators.build_taxi_tariff_tooltip_icon_locator(taxi_tariff_number))
            tooltip_is_displayed = self.check_taxi_tariff_tooltip_displayed(taxi_tariff_number)
            if not tooltip_is_displayed:
                self.wait_element_is_visible(self.locators.build_taxi_tariff_tooltip_icon_locator(taxi_tariff_number))
                self.hover_element(self.locators.build_taxi_tariff_tooltip_icon_locator(taxi_tariff_number))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error while hovering the taxi tariff icon: {e}")

    @allure.step('Verify that tariff tooltip is displayed.')
    def check_taxi_tariff_tooltip_displayed(self, taxi_tariff_number):
        if self.wait_element_is_visible(self.locators.build_taxi_tariff_tooltip_locator(taxi_tariff_number)):
            return True
        else:
            return False

    @allure.step('Check the taxi tariff name in the tooltip.')
    def check_taxi_tariff_name_in_tooltip(self, taxi_tariff):
        self.wait_element_is_visible(self.locators.build_taxi_tariff_tooltip_name(taxi_tariff))
        return self.get_element_text(self.locators.build_taxi_tariff_tooltip_name(taxi_tariff))

    @allure.step('Check the taxi tariff description in the tooltip.')
    def check_taxi_tariff_description_in_tooltip(self, taxi_tariff):
        self.wait_element_is_visible(self.locators.build_taxi_tariff_tooltip_description(taxi_tariff))
        return self.get_element_text(self.locators.build_taxi_tariff_tooltip_description(taxi_tariff))

    @allure.step('Verify that the field is displayed in the taxi order form.')
    def check_field_is_displayed_in_order_taxi_form(self, locator):
        if self.wait_element_is_visible(locator):
            return True
        else:
            return False

    @allure.step('Click on "For work" taxi tariff.')
    def wait_click_on_for_work_taxi_tariff(self):
        self.wait_element_is_visible(self.locators.build_taxi_tariff_card_locator(RoutePageData.TAXI_TARIFFS[0]))
        self.click_on_element(self.locators.build_taxi_tariff_card_locator(RoutePageData.TAXI_TARIFFS[0]))

    @allure.step('Click on "Order requirements" element.')
    def wait_click_on_order_requirements_element(self):
        self.wait_element_is_visible(self.locators.AB_POINTS_ROUTE)
        self.scroll_to_element(self.locators.ORDER_REQUIREMENTS)
        self.wait_element_is_visible(self.locators.ORDER_REQUIREMENTS)
        self.click_on_element(self.locators.ORDER_REQUIREMENTS)

    @allure.step('Click on "Table for notebook" toggle.')
    def wait_click_on_toggle_notebook_table(self):
        self.wait_element_is_visible(self.locators.NOTEBOOK_TABLE_TOGGLE)
        self.click_on_element(self.locators.NOTEBOOK_TABLE_TOGGLE)

    @allure.step('Click on "Enter number and order" button.')
    def wait_click_on_order_taxi_button(self):
        self.wait_element_is_visible(self.locators.ORDER_TAXI_BUTTON)
        self.click_on_element(self.locators.ORDER_TAXI_BUTTON)

    @allure.step('Verify that the order taxi popup displayed.')
    def check_order_taxi_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.TAXI_ORDER_POPUP):
            return True
        else:
            return False

    @allure.step('Check the heading in the "Search a taxi" popup.')
    def check_heading_in_search_taxi_popup(self):
        self.wait_element_is_visible(self.locators.SEARCH_TAXI_POPUP_HEADING)
        return self.get_element_text(self.locators.SEARCH_TAXI_POPUP_HEADING)

    @allure.step('Verify that the time counter is displayed in "Search a taxi" popup.')
    def check_time_counter_in_search_taxi_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.SEARCH_TAXI_POPUP_TIME_COUNTER):
            return True
        else:
            return False

    @allure.step('Verify that the "Cancel" button is displayed in the popup.')
    def check_cancel_button_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.POPUP_CANCEL_BUTTON):
            return True
        else:
            return False

    @allure.step('Verify that the "Details" button is displayed in the popup.')
    def check_details_button_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.POPUP_DETAILS_BUTTON):
            return True
        else:
            return False

    @allure.step('Verify that the "Details" button is displayed in the popup.')
    def check_details_button_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.POPUP_DETAILS_BUTTON):
            return True
        else:
            return False

    @allure.step('Verify that the "Details" button is displayed in the popup.')
    def check_details_button_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.POPUP_DETAILS_BUTTON):
            return True
        else:
            return False

    @allure.step('Wait until the time counter is not displayed.')
    def wait_time_counter_is_not_displayed(self):
        try:
            self.wait_element_is_not_displayed(self.locators.SEARCH_TAXI_POPUP_TIME_COUNTER)
        except TimeoutException as e:
            raise AssertionError('Time counter did not disappear within the expected time.') from e

    @allure.step('Check the heading in the completed order popup.')
    def check_heading_in_completed_order_popup(self):
        self.wait_element_is_visible(self.locators.COMPLETED_ORDER_POPUP_HEADING)
        return self.get_element_text(self.locators.COMPLETED_ORDER_POPUP_HEADING)

    @allure.step('Verify that the car number is displayed in the popup.')
    def check_car_number_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.CAR_NUMBER):
            return True
        else:
            return False

    @allure.step('Verify that the taxi tariff image is displayed in the popup.')
    def check_taxi_tariff_image_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.TAXI_TARIFF_IMAGE):
            return True
        else:
            return False

    @allure.step('Verify that the driver name is displayed in the popup.')
    def check_driver_name_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.DRIVER_NAME):
            return True
        else:
            return False

    @allure.step('Verify that the driver image is displayed in the popup.')
    def check_driver_image_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.DRIVER_IMAGE):
            return True
        else:
            return False

    @allure.step('Verify that the driver rating is displayed in the popup.')
    def check_driver_rating_in_popup_is_displayed(self):
        if self.wait_element_is_visible(self.locators.DRIVER_RATING):
            return True
        else:
            return False

    @allure.step('Click on "Details" button in the completed order popup.')
    def wait_click_on_details_button_in_popup(self):
        self.wait_element_is_visible(self.locators.POPUP_DETAILS_BUTTON)
        self.click_on_element(self.locators.POPUP_DETAILS_BUTTON)

    @allure.step('Check the initial drive price for "For work" taxi tariff.')
    def check_initial_price_for_work_taxi_tariff(self):
        self.wait_element_is_visible(self.locators.AB_POINTS_ROUTE)
        self.wait_element_is_visible(self.locators.DRIVE_PRICE_INITIAL_FOR_WORK_TAXI_TARIFF)
        price_with_currency = self.get_element_text(self.locators.DRIVE_PRICE_INITIAL_FOR_WORK_TAXI_TARIFF)
        price_value = ''.join(filter(str.isdigit, price_with_currency))
        return price_value

    @allure.step('Check the drive price in details section in popup.')
    def check_final_price_for_work_taxi_tariff(self):
        self.wait_element_is_visible(self.locators.DRIVE_PRICE_IN_DETAILS_SECTION)
        price_with_text = self.get_element_text(self.locators.DRIVE_PRICE_IN_DETAILS_SECTION)
        price_value = ''.join(filter(str.isdigit, price_with_text))
        return price_value

    @allure.step('Click on "Cancel" button in the completed order popup.')
    def wait_click_on_cancel_button_in_popup(self):
        self.wait_element_is_visible(self.locators.POPUP_CANCEL_BUTTON)
        self.click_on_element(self.locators.POPUP_CANCEL_BUTTON)
