from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.acciones import hacer_click, escribir


class LoginPage:
    """Página de login de SauceDemo."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Abre la página de login."""
        self.driver.get(self.URL)

    def login(self, usuario="standard_user", password="secret_sauce"):
        """Escribe el usuario y la contraseña, y hace click en el botón Login."""
        escribir(self.driver, self.driver.find_element(By.ID, "user-name"), usuario)
        escribir(self.driver, self.driver.find_element(By.ID, "password"), password)
        hacer_click(self.driver, self.driver.find_element(By.ID, "login-button"))
        # Esperamos a que cargue la página de productos antes de seguir
        self.wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))
