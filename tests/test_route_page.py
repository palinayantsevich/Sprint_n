import allure
import pytest

from locators import RoutePageLocators

from data import RoutePageData


class TestRoutePage:

    @allure.title(
        'SCENARIO #1.1: Verify that if user specifies different addresses in "from" and "to" fields - points A (from) and B (where) are displayed on the map.')
    @pytest.mark.parametrize(
        'from_address,where_address',
        [
            (RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD),
            (RoutePageData.ADDRESS_ZUB_BLVD, RoutePageData.ADDRESS_HAM_VAL)
        ]
    )
    def test_ab_points_displayed_on_map_if_specify_from_and_to_fields(self, route_page, from_address, where_address):
        route_page.wait_fill_from_field(from_address)
        route_page.wait_fill_where_field(where_address)
        points_list = route_page.find_ab_points_on_map()
        assert len(points_list) == 2

    @allure.title(
        'SCENARIO #1.2: Verify that the placeholder texts are correct in the "from" and "to" fields.')
    def test_placeholder_texts_in_from_and_to_fields(self, route_page):
        from_field_text = route_page.check_from_field_placeholder_text()
        to_field_text = route_page.check_to_field_placeholder_text()
        assert from_field_text == RoutePageData.FROM_FIELD_PLACEHOLDER
        assert to_field_text == RoutePageData.TO_FIELD_PLACEHOLDER

    @allure.title(
        'SCENARIO #2.1: Verify that if user specifies different addresses in "from" and "to" fields - route selection section is displayed.')
    def test_route_section_displayed_if_specify_different_addresses(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_section_is_displayed = route_page.check_route_section_displayed()
        assert route_section_is_displayed == True

    @allure.title(
        'SCENARIO #2.2: Verify that if user specifies same addresses in "from" and "to" fields - special text and duration is is displayed in the route selection section.')
    def test_route_section_text_and_duration_if_specify_same_addresses(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_HAM_VAL)
        text_route_section = route_page.check_route_section_price_text()
        duration_route_section = route_page.check_route_section_duration_text()
        assert text_route_section == RoutePageData.TEXT_ROUTE_SECTION_SAME_ADDRESSES
        assert duration_route_section == RoutePageData.DURATION_ROUTE_SECTION_SAME_ADDRESSES

    @allure.title(
        'SCENARIO #3.1.1: Verify that if user specifies different addresses in "from" and "to" fields - "Optimal" route can be selected in the route selection section and text and duration values are recalculated.')
    @pytest.mark.xfail(
        reason='Legacy bug: duration value is not recalculated when switching between "Fast" and "Optimal" tabs.')
    def test_optimal_route_selected_in_route_section_if_entered_different_addresses(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        fast_tab_state = route_page.check_fast_tab_is_active()
        fast_tab_price = route_page.check_route_section_price_value()
        fast_tab_duration = route_page.check_route_section_duration_value()
        route_page.wait_click_on_optimal_tab()
        optimal_tab_state = route_page.check_optimal_tab_is_active()
        optimal_tab_price = route_page.check_route_section_price_value()
        optimal_tab_duration = route_page.check_route_section_duration_value()
        assert RoutePageData.ACTIVE_ELEMENT_PROPERTY in fast_tab_state
        assert RoutePageData.ACTIVE_ELEMENT_PROPERTY in optimal_tab_state
        assert optimal_tab_price != fast_tab_price
        assert optimal_tab_duration != fast_tab_duration

    @allure.title(
        'SCENARIO #3.2: Verify that if user specifies different addresses in "from" and "to" fields - "Personal" route can be selected in the route selection section and all movement types are available.')
    @pytest.mark.parametrize('movement_type', RoutePageData.MOVEMENT_TYPES)
    def test_personal_route_selected_in_route_section_if_entered_different_addresses(self, route_page, movement_type):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_personal_tab()
        personal_tab_state = route_page.check_personal_tab_is_active()
        movement_type_state = route_page.check_movement_type_state(movement_type)
        assert RoutePageData.ACTIVE_ELEMENT_PROPERTY in personal_tab_state
        assert RoutePageData.DISABLED_ELEMENT_PROPERTY not in movement_type_state

    @allure.title('SCENARIO #3.3: Verify that "Get Taxi" button is clickable if select "Fast" route section.')
    def test_get_taxi_button_is_clickable_if_fast_route_selected(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        tariff_picker_section_is_displayed = route_page.check_taxi_tariff_section_displayed()
        assert tariff_picker_section_is_displayed == True

    @allure.title(
        'SCENARIO #3.4: Verify that "Book" button is clickable if select "Personal" route section and "Drive" movement type.')
    def test_book_button_is_clickable_if_drive_movement_type_selected(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_personal_tab()
        route_page.wait_click_on_drive_movement_icon()
        route_page.wait_click_on_book_button()
        tariff_picker_section_is_displayed = route_page.check_taxi_tariff_section_displayed()
        assert tariff_picker_section_is_displayed == True

    @allure.title(
        'SCENARIO #4.1.1: Verify that if user selects "Fast" route and click on "Get Taxi" button - 6 taxi tariff types are available.')
    @pytest.mark.parametrize('taxi_tariff', RoutePageData.TAXI_TARIFFS)
    def test_fast_route_selected_available_taxi_tariffs(self, route_page, taxi_tariff):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        taxi_tariff_is_displayed = route_page.wait_check_taxi_tariff_displayed(taxi_tariff)
        assert taxi_tariff_is_displayed == True

    @allure.title(
        'SCENARIO #4.1.2: Verify that if user selects "Fast" route and click on "Get Taxi" button - only 1 taxi tariff is active.')
    def test_fast_route_selected_only_one_active_taxi_tariff(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        active_taxi_tariff = route_page.find_active_taxi_tariffs()
        assert len(active_taxi_tariff) == 1

    @allure.title(
        'SCENARIO #4.2: Verify that if hover tooltip icon in each taxi tariff card - the tooltip with taxi tariff name and description is displayed.')
    @pytest.mark.xfail(reason='Legacy bug for incorrect description for "Сонный" and "Разговорчивый" taxi tariffs.')
    @pytest.mark.parametrize('taxi_tariff_number,taxi_tariff,taxi_tariff_description',
                             [
                                 (RoutePageData.TAXI_TARIFFS_NUMBERS[0], RoutePageData.TAXI_TARIFFS[0],
                                  RoutePageData.TAXI_TARIFFS_DESCRIPTION[0]),
                                 (RoutePageData.TAXI_TARIFFS_NUMBERS[1], RoutePageData.TAXI_TARIFFS[1],
                                  RoutePageData.TAXI_TARIFFS_DESCRIPTION[1]),
                                 (RoutePageData.TAXI_TARIFFS_NUMBERS[2], RoutePageData.TAXI_TARIFFS[2],
                                  RoutePageData.TAXI_TARIFFS_DESCRIPTION[2]),
                                 (RoutePageData.TAXI_TARIFFS_NUMBERS[3], RoutePageData.TAXI_TARIFFS[3],
                                  RoutePageData.TAXI_TARIFFS_DESCRIPTION[3]),
                                 (RoutePageData.TAXI_TARIFFS_NUMBERS[4], RoutePageData.TAXI_TARIFFS[4],
                                  RoutePageData.TAXI_TARIFFS_DESCRIPTION[4]),
                                 (RoutePageData.TAXI_TARIFFS_NUMBERS[5], RoutePageData.TAXI_TARIFFS[5],
                                  RoutePageData.TAXI_TARIFFS_DESCRIPTION[5]),
                             ]
                             )
    def test_taxi_tariffs_data_in_tooltips(self, route_page, taxi_tariff_number, taxi_tariff, taxi_tariff_description):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        route_page.wait_click_on_taxi_tariff(taxi_tariff)
        route_page.wait_hover_taxi_tariff_tooltip(taxi_tariff_number)
        actual_taxi_tariff_name = route_page.check_taxi_tariff_name_in_tooltip(taxi_tariff)
        actual_taxi_tariff_description = route_page.check_taxi_tariff_description_in_tooltip(taxi_tariff)
        assert actual_taxi_tariff_name == taxi_tariff
        assert actual_taxi_tariff_description == taxi_tariff_description

    @allure.title(
        'SCENARIO #4.3: Verify that "Phone", "Payment method", "Comment", "Order requirements" fields are displayed in taxi tariff order form.')
    @pytest.mark.parametrize('locator',
                             [
                                 RoutePageLocators.PHONE_FIELD,
                                 RoutePageLocators.PAYMENT_METHOD_FIELD,
                                 RoutePageLocators.COMMENT_FIELD,
                                 RoutePageLocators.ORDER_REQUIREMENTS
                             ]
                             )
    def test_field_is_displayed_in_order_taxi_form(self, route_page, locator):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        field_is_displayed = route_page.check_field_is_displayed_in_order_taxi_form(locator)
        assert field_is_displayed == True

    @allure.title(
        'SCENARIO #5.1: Verify that if user selects "For work" taxi tariff and order taxi with "Table for notebook" option enabled - search a taxi popup is displayed correctly.')
    def test_search_taxi_popup_elements_if_taxi_ordered_with_enabled_notebook_table_option(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        route_page.wait_click_on_for_work_taxi_tariff()
        route_page.wait_click_on_order_requirements_element()
        route_page.wait_click_on_toggle_notebook_table()
        route_page.wait_click_on_order_taxi_button()
        search_taxi_popup_is_displayed = route_page.check_order_taxi_popup_is_displayed()
        search_taxi_popup_heading = route_page.check_heading_in_search_taxi_popup()
        time_counter_is_displayed = route_page.check_time_counter_in_search_taxi_popup_is_displayed()
        cancel_button_is_displayed = route_page.check_cancel_button_in_popup_is_displayed()
        details_button_is_displayed = route_page.check_details_button_in_popup_is_displayed()
        assert search_taxi_popup_is_displayed == True
        assert search_taxi_popup_heading == RoutePageData.SEARCH_TAXI_POPUP_HEADING
        assert time_counter_is_displayed == True
        assert cancel_button_is_displayed == True
        assert details_button_is_displayed == True

    @allure.title(
        'SCENARIO #5.2: Verify that if user selects "For work" taxi tariff and order taxi with "Table for notebook" option enabled - search a taxi popup is displayed correctly.')
    def test_completed_order_popup_elements_if_taxi_ordered_with_enabled_notebook_table_option(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        route_page.wait_click_on_for_work_taxi_tariff()
        route_page.wait_click_on_order_requirements_element()
        route_page.wait_click_on_toggle_notebook_table()
        route_page.wait_click_on_order_taxi_button()
        route_page.wait_time_counter_is_not_displayed()
        completed_order_popup_heading = route_page.check_heading_in_completed_order_popup()
        car_number_is_displayed = route_page.check_car_number_in_popup_is_displayed()
        taxi_tariff_image_is_displayed = route_page.check_taxi_tariff_image_in_popup_is_displayed()
        driver_name_is_displayed = route_page.check_driver_name_in_popup_is_displayed()
        driver_image_is_displayed = route_page.check_driver_image_in_popup_is_displayed()
        driver_rating_is_displayed = route_page.check_driver_rating_in_popup_is_displayed()
        cancel_button_is_displayed = route_page.check_cancel_button_in_popup_is_displayed()
        details_button_is_displayed = route_page.check_details_button_in_popup_is_displayed()
        assert RoutePageData.COMPLETED_ORDER_POPUP_HEADING in completed_order_popup_heading
        assert car_number_is_displayed == True
        assert taxi_tariff_image_is_displayed == True
        assert driver_name_is_displayed == True
        assert driver_image_is_displayed == True
        assert driver_rating_is_displayed == True
        assert cancel_button_is_displayed == True
        assert details_button_is_displayed == True

    @allure.title(
        'SCENARIO #5.3: Verify that initial drive price in "For work" taxi tariff card is the same as in details section in completed order popup.')
    def test_compare_initial_and_final_price_for_work_taxi_tariff(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        route_page.wait_click_on_for_work_taxi_tariff()
        initial_price = route_page.check_initial_price_for_work_taxi_tariff()
        route_page.wait_click_on_order_requirements_element()
        route_page.wait_click_on_toggle_notebook_table()
        route_page.wait_click_on_order_taxi_button()
        route_page.wait_time_counter_is_not_displayed()
        route_page.wait_click_on_details_button_in_popup()
        final_price = route_page.check_final_price_for_work_taxi_tariff()
        assert initial_price == final_price

    @allure.title(
        'SCENARIO #5.4: Verify that completed order popup is not displayed after clicking on "Cancel" button.')
    @pytest.mark.xfail(reason='Legacy bug: "Cancel" button is not working.')
    def test_taxi_popup_closed_if_click_cancel_button(self, route_page):
        route_page.wait_fill_from_and_where_fields(RoutePageData.ADDRESS_HAM_VAL, RoutePageData.ADDRESS_ZUB_BLVD)
        route_page.wait_click_on_fast_tab()
        route_page.wait_click_on_get_taxi_button()
        route_page.wait_click_on_for_work_taxi_tariff()
        route_page.wait_click_on_order_requirements_element()
        route_page.wait_click_on_toggle_notebook_table()
        route_page.wait_click_on_order_taxi_button()
        route_page.wait_time_counter_is_not_displayed()
        route_page.wait_click_on_cancel_button_in_popup()
        order_popup_is_displayed = route_page.check_order_taxi_popup_is_displayed()
        assert order_popup_is_displayed == False
