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

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_overlays_to_disappear(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    self.MODAL_OVERLAY
                )
            )
        except TimeoutException:
            # Если overlay всё ещё есть,
            # проверяем, действительно ли он отображается.
            overlays = self.driver.find_elements(
                *self.MODAL_OVERLAY
            )

            visible_overlays = [
                overlay
                for overlay in overlays
                if overlay.is_displayed()
            ]

            if visible_overlays:
                # Убираем зависший overlay через JS.
                self.driver.execute_script(
                    """
                    arguments[0].style.display = 'none';
                    """,
                    visible_overlays[0]
                )

    def click_element(self, locator):
        self.wait_for_overlays_to_disappear()

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            element
        )

        self.wait_for_overlays_to_disappear()

        try:
            element.click()
        except Exception:
            # Firefox иногда всё ещё считает overlay препятствием,
            # хотя элемент уже кликабельный.
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def get_text(self, locator):
        return self.find_element(locator).text

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

    def is_element_invisible(self, locator):
        return WebDriverWait(
            self.driver,
            5
        ).until(
            EC.invisibility_of_element_located(locator)
        )

    def close_modal(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def wait_for_modal_to_close(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                self.MODAL_OVERLAY
            )
        )