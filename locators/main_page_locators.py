from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[@href='/']"
    )

    FEED_BUTTON = (
        By.XPATH,
        "//a[@href='/feed']"
    )

    INGREDIENT_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']/parent::div"
    )

    CLOSE_MODAL_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )

    BUN_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    MAIN_INGREDIENT_CARD = (
        By.XPATH,
        "//a[.//p[text()='Биокотлета из марсианской Магнолии']]"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[text()='Биокотлета из марсианской Магнолии']"
        "/ancestor::a"
        "//p[contains(@class, 'counter_counter__num')]"
    )

    MAKE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]"
    )

    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'text_type_digits-large')]"
    )

    ORDER_MODAL_CLOSE = (
        By.XPATH,
        "//div[contains(@class, 'modal')]//button"
    )

    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    )

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        ".Modal_modal_overlay__x2ZCr"
    )