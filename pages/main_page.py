import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import MAIN_PAGE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(MAIN_PAGE_URL)

    @allure.step("Перейти в раздел «Конструктор»")
    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_BUTTON
        )

    @allure.step("Перейти в раздел «Лента заказов»")
    def click_feed(self):
        self.click_element(
            MainPageLocators.FEED_BUTTON
        )

    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_element(
            MainPageLocators.INGREDIENT_CARD
        )

    @allure.step("Закрыть окно с деталями ингредиента")
    def close_ingredient_modal(self):
        self.close_modal(
            MainPageLocators.CLOSE_MODAL_BUTTON
        )

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        elements = self.find_elements_without_wait(
            MainPageLocators.INGREDIENT_COUNTER
        )

        if not elements:
            return 0

        return int(elements[0].text)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient(self):
        ingredient = self.find_element(
            MainPageLocators.MAIN_INGREDIENT_CARD
        )

        drop_zone = self.find_element(
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

        self.scroll_to_element(ingredient)
        self.scroll_to_element(drop_zone)

        self.drag_and_drop_by_javascript(
            ingredient,
            drop_zone
        )

    @allure.step("Дождаться увеличения счётчика ингредиента")
    def wait_for_ingredient_counter_increase(self, initial_counter):
        self.wait.until(
            lambda driver: self.get_ingredient_counter() > initial_counter
        )

    @allure.step("Добавить булку и ингредиент в конструктор")
    def add_burger_ingredients(self):
        bun = self.find_element(
            MainPageLocators.BUN_CARD
        )

        ingredient = self.find_element(
            MainPageLocators.MAIN_INGREDIENT_CARD
        )

        drop_zone = self.find_element(
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

        for item in [bun, ingredient]:
            self.scroll_to_element(item)
            self.drag_and_drop_by_javascript(
                item,
                drop_zone
            )

    @allure.step("Перенести элемент в конструктор")
    def drag_and_drop_by_javascript(self, source, target):
        self.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
            """,
            source,
            target
        )

    @allure.step("Оформить заказ")
    def make_order(self):
        self.click_element(
            MainPageLocators.MAKE_ORDER_BUTTON
        )

    @allure.step("Получить номер созданного заказа")
    def get_order_number(self):
        def order_number_is_ready(driver):
            number = self.get_text(
                MainPageLocators.ORDER_NUMBER
            )

            if (
                number
                and number != "9999"
                and number.isdigit()
            ):
                return number

            return False

        return self.wait.until(order_number_is_ready)