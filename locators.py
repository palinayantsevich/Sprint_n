from selenium.webdriver.common.by import By


class RoutePageLocators:
    FROM_FIELD = (By.XPATH, '//input[@placeholder="Хамовнический Вал, 18"]')
    FROM_FIELD_PLACEHOLDER = (By.XPATH, '//label[text()="Откуда"]')
    TO_FIELD = (By.XPATH, '//input[@placeholder="Льва Толстого, 16"]')
    TO_FIELD_PLACEHOLDER = (By.XPATH, '//label[text()="Куда"]')
    AB_POINTS_ROUTE = (By.XPATH, '//ymaps[@class="ymaps-2-1-79-placemark-overlay ymaps-2-1-79-user-selection-none"]')
    ROUTE_SECTION = (By.XPATH, '//div[@class="type-picker shown"]')
    ROUTE_SECTION_TEXT = (By.XPATH, '//div[@class="text"]')
    ROUTE_SECTION_DURATION = (By.XPATH, '//div[@class="duration"]')

    OPTIMAL_ROUTE_TAB = (By.XPATH, '//div[text()="Оптимальный"]')

    FAST_ROUTE_TAB = (By.XPATH, '//div[text()="Быстрый"]')
    GET_TAXI_BUTTON = (By.XPATH, '//button[text()="Вызвать такси"]')
    TARIFF_PICKER_SECTION = (By.XPATH, '//div[@class="tariff-picker shown"]')
    ACTIVE_TAXI_TARIFF = (By.XPATH, '//div[@class="tcard active"]')
    BACK_BUTTON = (By.XPATH, '//button[@class="arrow-button tariffs-arrow-button"]')
    PHONE_FIELD = (By.XPATH, '//div[@class="np-button"]')
    PAYMENT_METHOD_FIELD = (By.XPATH, '//div[@class="pp-button filled"]')
    COMMENT_FIELD = (By.XPATH, '//label[@class="label" and contains(text(), "Комментарий водителю...")]/parent::div')
    ORDER_REQUIREMENTS = (By.XPATH, '//div[@class="reqs-header"]')
    NOTEBOOK_TABLE_TOGGLE = (By.XPATH, '//span[@class="slider round"]')
    ORDER_TAXI_BUTTON = (By.XPATH, '//span[text()="Ввести номер и заказать"]/parent::button[@class="smart-button"]')

    TAXI_ORDER_POPUP = (By.XPATH, '//div[@class="order-body"]')
    SEARCH_TAXI_POPUP_HEADING = (By.XPATH, '//div[text()="Поиск машины"]')
    SEARCH_TAXI_POPUP_TIME_COUNTER = (By.XPATH, '//div[@class="order-header-time"]')
    POPUP_CANCEL_BUTTON = (By.XPATH, '//div[text()="Отменить"]/preceding-sibling::button')
    POPUP_DETAILS_BUTTON = (By.XPATH, '//div[text()="Детали"]/preceding-sibling::button')
    COMPLETED_ORDER_POPUP_HEADING = (By.XPATH, '//div[text()=" мин. и приедет"]')
    CAR_NUMBER = (By.XPATH, '//div[@class="number"]')
    TAXI_TARIFF_IMAGE = (By.XPATH, '//div[@class="order-number"]/img[@src="/static/media/economy.61e4a774.svg"]')
    DRIVER_NAME = (By.XPATH, '//div[@class="order-button"]/following-sibling::div')
    DRIVER_IMAGE = (By.XPATH, '//div[@class="order-btn-rating"]/following-sibling::img')
    DRIVER_RATING = (By.XPATH, '//div[@class="order-btn-rating"]')
    DRIVE_PRICE_INITIAL_FOR_WORK_TAXI_TARIFF = (
        By.XPATH, '//div[@class="tcard-title" and text()="Рабочий"]/following-sibling::div[@class="tcard-price"]')
    DRIVE_PRICE_IN_DETAILS_SECTION = (
        By.XPATH, '//div[text()="Еще про поездку"]/following-sibling::div[@class="o-d-sh"]')

    PERSONAL_ROUTE_TAB = (By.XPATH, '//div[text()="Свой"]')
    CAR_MOVEMENT_TYPE = (By.XPATH, '//img[@class="type-icon" and contains(@src, "car")]')
    DRIVE_MOVEMENT_TYPE = (By.XPATH, '//img[@class="type-icon" and contains(@src, "drive")]')
    BOOK_BUTTON = (By.XPATH, '//button[text()="Забронировать"]')

    def build_movement_type_locator(self, movement_type):
        return (By.XPATH, f'//img[@class="type-icon" and contains(@src, "{movement_type}")]/parent::div')

    def build_taxi_tariff_card_locator(self, taxi_tariff):
        return (By.XPATH, f'//div[@class="tcard-title" and text()="{taxi_tariff}"]/parent::div')

    def build_taxi_tariff_tooltip_icon_locator(self, taxi_tariff_number):
        return (By.XPATH, f'//div[@class="tcard active"]/button[@data-for="tariff-card-{taxi_tariff_number}"]')

    def build_taxi_tariff_tooltip_locator(self, taxi_tariff_number):
        return (By.XPATH, f'//div[@id="tariff-card-{taxi_tariff_number}" and contains(@class, "show")]')

    def build_taxi_tariff_tooltip_name(self, taxi_tariff):
        return (By.XPATH, f'//div[@class="i-title" and contains(text(), "{taxi_tariff}")]')

    def build_taxi_tariff_tooltip_description(self, taxi_tariff):
        return (By.XPATH,
                f'//div[@class="i-title" and contains(text(), "{taxi_tariff}")]/following-sibling::div[@class="i-dPrefix"]')
