from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.acciones import hacer_click


class InventoryPage:
    """Página de productos (inventario) de SauceDemo."""

    def __init__(self, driver):
        self.driver = driver

    def sort_by(self, valor):
        """Ordena los productos. Valores posibles: 'az', 'za', 'lohi', 'hilo'."""
        combo = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        combo.select_by_value(valor)

    def get_prices(self):
        """Devuelve la lista de precios convertidos a número (ej: [7.99, 9.99])."""
        precios = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(p.text.replace("$", "")) for p in precios]

    def get_product_names(self):
        """Devuelve la lista de nombres de los productos."""
        nombres = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [n.text for n in nombres]

    def add_all_to_cart(self):
        """Agrega todos los productos al carrito."""
        for boton in self.driver.find_elements(By.CSS_SELECTOR, ".btn_inventory"):
            hacer_click(self.driver, boton)

    def add_first_to_cart(self):
        """Agrega el primer producto al carrito."""
        boton = self.driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")[0]
        hacer_click(self.driver, boton)

    def add_two_to_cart(self):
        """Agrega los primeros dos productos al carrito."""
        botones = self.driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
        hacer_click(self.driver, botones[0])
        hacer_click(self.driver, botones[1])

    def go_to_cart(self):
        """Hace click en el ícono del carrito para ir a verlo."""
        boton = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        hacer_click(self.driver, boton)
