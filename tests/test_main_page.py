import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title("Переход в раздел Конструктор")
    def test_click_constructor_opens_constructor(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        main_page = MainPage(driver)
        main_page.click_constructor()

        assert "stellarburgers.education-services.ru" in driver.current_url
        assert "/feed" not in driver.current_url

    @allure.title("Переход в раздел Лента заказов")
    def test_click_feed_opens_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_feed()

        assert "/feed" in driver.current_url

    @allure.title("Открывается окно с деталями ингредиента")
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_ingredient_details()

        assert main_page.is_element_visible(
            MainPageLocators.INGREDIENT_DETAILS_TITLE
        )

    @allure.title("Окно с деталями ингредиента закрывается по крестику")
    def test_ingredient_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_ingredient_details()
        main_page.close_ingredient_modal()

        assert main_page.is_element_invisible(
            MainPageLocators.INGREDIENT_DETAILS_TITLE
        )

    @allure.title("При добавлении ингредиента увеличивается счётчик")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        initial_counter = main_page.get_ingredient_counter()

        main_page.add_ingredient()

        main_page.wait_for_ingredient_counter_increase(initial_counter)

        new_counter = main_page.get_ingredient_counter()

        assert new_counter > initial_counter