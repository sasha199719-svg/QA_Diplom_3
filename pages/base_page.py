import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        ".Modal_modal_overlay__x2ZCr"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Дождаться исчезновения overlay")
    def wait_for_overlays_to_disappear(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    self.MODAL_OVERLAY
                )
            )
        except TimeoutException:
            overlays = self.find_elements_without_wait(
                self.MODAL_OVERLAY
            )

            visible_overlays = [
                overlay
                for overlay in overlays
                if overlay.is_displayed()
            ]

            if visible_overlays:
                self.execute_script(
                    """
                    arguments[0].style.display = 'none';
                    """,
                    visible_overlays[0]
                )

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )
    @allure.step("Найти элементы без ожидания")
    def find_elements_without_wait(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(
                self.driver,
                3
            ).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить отсутствие элемента")
    def is_element_invisible(self, locator):
        return WebDriverWait(
            self.driver,
            5
        ).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        self.wait_for_overlays_to_disappear()

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.scroll_to_element(element)

        self.wait_for_overlays_to_disappear()

        try:
            element.click()
        except Exception:
            self.execute_script(
                "arguments[0].click();",
                element
            )

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, element):
        self.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            element
        )

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(
            script,
            *args
        )

    @allure.step("Закрыть модальное окно")
    def close_modal(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_to_close(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                self.MODAL_OVERLAY
            )
        )