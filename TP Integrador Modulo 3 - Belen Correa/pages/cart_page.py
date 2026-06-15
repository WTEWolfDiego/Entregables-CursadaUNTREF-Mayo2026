from selenium.webdriver.common.by import By
from pages.acciones import hacer_click


class CartPage:
    """Página del carrito de SauceDemo."""

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        """Devuelve los nombres de los productos que están en el carrito."""
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in items]

    def get_cart_item_count(self):
        """Devuelve cuántos productos hay en el carrito."""
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    def remove_first_item(self):
        """Quita el primer producto del carrito."""
        boton = self.driver.find_elements(By.CSS_SELECTOR, ".cart_button")[0]
        hacer_click(self.driver, boton)

    def go_to_checkout(self):
        """Hace click en Checkout para empezar la compra."""
        boton = self.driver.find_element(By.ID, "checkout")
        hacer_click(self.driver, boton)

    def go_to_continue_shopping(self):
        """Vuelve a la página de productos (Continue Shopping)."""
        boton = self.driver.find_element(By.ID, "continue-shopping")
        hacer_click(self.driver, boton)
