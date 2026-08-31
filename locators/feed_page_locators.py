from selenium.webdriver.common.by import By


class FeedPageLocators:

    PAGE_TITLE = (
        By.XPATH,
        "//h1[text()='Лента заказов']"
    )

    TOTAL_ORDERS = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    TODAY_ORDERS = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    IN_PROGRESS_TITLE = (
        By.XPATH,
        "//p[text()='В работе:']"
    )

    IN_PROGRESS_ORDERS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul//li"
    )

    ORDER_NUMBER_IN_FEED = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title__2L34m')]"
    )