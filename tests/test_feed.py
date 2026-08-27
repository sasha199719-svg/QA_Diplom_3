import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage


class TestFeed:

    @allure.title(
        "После создания заказа увеличивается счётчик Выполнено за всё время"
    )
    def test_total_orders_counter_increases(
            self, driver, user
    ):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        initial_total = feed_page.get_total_orders()

        print(f"Было выполнено всего: {initial_total}")

        self.create_order(driver, user)

        feed_page.open_feed_page()

        feed_page.wait_for_total_orders_increase(
            initial_total
        )

        new_total = feed_page.get_total_orders()

        print(f"Стало выполнено всего: {new_total}")

        assert new_total > initial_total

    @allure.title(
        "После создания заказа увеличивается счётчик Выполнено за сегодня"
    )
    def test_today_orders_counter_increases(
            self, driver, user
    ):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        initial_today = feed_page.get_today_orders()

        self.create_order(driver, user)

        feed_page.open_feed_page()

        feed_page.wait_for_today_orders_increase(
            initial_today
        )

        new_today = feed_page.get_today_orders()

        assert new_today > initial_today

    @allure.title(
        "Номер оформленного заказа появляется в разделе В работе"
    )
    def test_order_number_appears_in_progress(
            self, driver, user
    ):
        order_number = self.create_order(
            driver,
            user
        )

        print(f"Номер созданного заказа: {order_number}")

        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        feed_page.wait_for_order_in_progress(
            order_number
        )

        orders_in_progress = feed_page.get_orders_in_progress()

        print(f"Заказы в работе: {orders_in_progress}")

        assert any(
            str(order_number) in order
            or f"0{order_number}" in order
            for order in orders_in_progress
        )

    @staticmethod
    def create_order(driver, user):
        login_page = LoginPage(driver)
        login_page.open_login_page()

        login_page.login(
            user["email"],
            user["password"]
        )

        main_page = MainPage(driver)

        main_page.add_burger_ingredients()

        main_page.make_order()

        order_number = main_page.get_order_number()

        return order_number