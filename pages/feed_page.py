import allure

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from data import FEED_PAGE_URL


class FeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_feed_page(self):
        self.open_page(FEED_PAGE_URL)

    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_total_orders(self):
        return int(
            self.get_text(
                FeedPageLocators.TOTAL_ORDERS
            )
        )

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_orders(self):
        return int(
            self.get_text(
                FeedPageLocators.TODAY_ORDERS
            )
        )

    @allure.step(
        "Дождаться увеличения счётчика «Выполнено за всё время»"
    )
    def wait_for_total_orders_increase(self, initial_total):
        self.wait.until(
            lambda driver: self.get_total_orders() > initial_total
        )

    @allure.step(
        "Дождаться увеличения счётчика «Выполнено за сегодня»"
    )
    def wait_for_today_orders_increase(self, initial_today):
        self.wait.until(
            lambda driver: self.get_today_orders() > initial_today
        )

    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        return [
            element.text
            for element in self.find_elements(
                FeedPageLocators.IN_PROGRESS_ORDERS
            )
        ]

    @allure.step(
        "Дождаться появления заказа {order_number} в разделе «В работе»"
    )
    def wait_for_order_in_progress(self, order_number):
        self.wait.until(
            lambda driver: any(
                str(order_number) in order
                or f"0{order_number}" in order
                for order in self.get_orders_in_progress()
            )
        )