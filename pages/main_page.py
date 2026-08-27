from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import MAIN_PAGE_URL

class MainPage(BasePage):

    def open_main_page(self):
        self.open_page(MAIN_PAGE_URL)

    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_BUTTON
        )

    def click_feed(self):
        self.click_element(
            MainPageLocators.FEED_BUTTON
        )

    def open_ingredient_details(self):
        self.click_element(
            MainPageLocators.INGREDIENT_CARD
        )

    def close_ingredient_modal(self):
        self.close_modal(
            MainPageLocators.CLOSE_MODAL_BUTTON
        )

    def add_ingredient(self):
        ingredient = self.find_element(
            MainPageLocators.MAIN_INGREDIENT_CARD
        )

        drop_zone = self.find_element(
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            ingredient
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            drop_zone
        )

        self.driver.execute_script("""
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
        """, ingredient, drop_zone)
    def get_ingredient_counter(self):
        elements = self.driver.find_elements(
            *MainPageLocators.INGREDIENT_COUNTER
        )

        if not elements:
            return 0

        return int(elements[0].text)

    def wait_for_ingredient_counter_increase(self, initial_counter):
        self.wait.until(
            lambda driver: self.get_ingredient_counter() > initial_counter
        )

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
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                item
            )

            self.driver.execute_script(
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
                item,
                drop_zone
            )

    def make_order(self):
        self.click_element(
            MainPageLocators.MAKE_ORDER_BUTTON
        )

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

    def wait_for_modal_to_close(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.MODAL_OVERLAY
            )
        )