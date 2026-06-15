from selenium.webdriver.common.by import By
from pages.acciones import hacer_click, escribir


class CheckoutPage:
    """Página de checkout (datos de la compra) de SauceDemo."""

    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self, nombre):
        """Escribe el nombre."""
        campo = self.driver.find_element(By.ID, "first-name")
        escribir(self.driver, campo, nombre)

    def fill_last_name(self, apellido):
        """Escribe el apellido."""
        campo = self.driver.find_element(By.ID, "last-name")
        escribir(self.driver, campo, apellido)

    def fill_postal_code(self, codigo_postal):
        """Escribe el código postal."""
        campo = self.driver.find_element(By.ID, "postal-code")
        escribir(self.driver, campo, codigo_postal)

    def click_continue(self):
        """Hace click en Continue."""
        boton = self.driver.find_element(By.ID, "continue")
        hacer_click(self.driver, boton)

    def click_finish(self):
        """Hace click en Finish para finalizar la compra."""
        boton = self.driver.find_element(By.ID, "finish")
        hacer_click(self.driver, boton)

    def get_error_message(self):
        """Devuelve el texto del mensaje de error (ej: 'Error: Last Name is required')."""
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text

    def get_confirmation_header(self):
        """Devuelve el texto de confirmación de la compra (ej: 'Thank you for your order!')."""
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
