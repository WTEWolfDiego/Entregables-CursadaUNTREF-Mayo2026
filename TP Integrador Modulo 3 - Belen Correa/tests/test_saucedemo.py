import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSauceDemo:
    """Tests de UI para https://www.saucedemo.com/"""

    def test_caso1_ordenar_por_precio_low_to_high(self, driver):
        """
        Caso 1:
        - Login como standard_user
        - Ordenar productos por precio (low to high)
        - Verificar que los precios están ordenados de menor a mayor
        """
        # Arrange
        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        # Act
        login.open()
        login.login()
        inventory.sort_by("lohi")

        # Assert
        prices = inventory.get_prices()
        assert prices == sorted(prices), (
            f"Los productos NO están ordenados de menor a mayor.\n"
            f"Precios obtenidos: {prices}\n"
            f"Precios esperados: {sorted(prices)}"
        )

    def test_caso2_checkout_validaciones_campos(self, driver):
        """
        Caso 2:
        - Login como standard_user
        - Agregar todos los productos al carrito
        - Verificar que todos están en el carrito
        - Ir al checkout e ingresar solo el nombre → error Last Name required
        - Ingresar apellido → error Postal Code required
        """
        # Arrange
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        # Act - Login y agregar todos los productos
        login.open()
        login.login()

        # Necesitamos saber cuántos productos hay antes de agregarlos
        product_names = inventory.get_product_names()
        total_products = len(product_names)

        inventory.add_all_to_cart()
        inventory.go_to_cart()

        # Assert - Verificar que todos los elementos están en el carrito
        cart_items = cart.get_cart_items()
        assert len(cart_items) == total_products, (
            f"Se esperaban {total_products} ítems en el carrito, "
            f"pero hay {len(cart_items)}: {cart_items}"
        )

        # Act - Ir al checkout e ingresar solo nombre
        cart.go_to_checkout()
        checkout.fill_first_name("Belén")
        checkout.click_continue()

        # Assert - Error por falta de apellido
        error_msg = checkout.get_error_message()
        assert "Last Name is required" in error_msg, (
            f"Se esperaba error 'Last Name is required', se obtuvo: '{error_msg}'"
        )

        # Act - Ingresar apellido y continuar
        checkout.fill_last_name("García")
        checkout.click_continue()

        # Assert - Error por falta de código postal
        error_msg = checkout.get_error_message()
        assert "Postal Code is required" in error_msg, (
            f"Se esperaba error 'Postal Code is required', se obtuvo: '{error_msg}'"
        )

    def test_caso3_flujo_completo_compra(self, driver):
        """
        Caso 3:
        - Login como standard_user
        - Agregar 1 ítem, ir al carrito, removerlo
        - Verificar carrito vacío
        - Continue shopping, agregar 2 ítems
        - Ir al carrito y verificar que existen
        - Hacer checkout completo
        - Verificar que la compra fue realizada
        """
        # Arrange
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        # Act - Login y agregar 1 producto
        login.open()
        login.login()
        inventory.add_first_to_cart()
        inventory.go_to_cart()

        # Act - Remover el ítem
        cart.remove_first_item()

        # Assert - Carrito vacío
        item_count = cart.get_cart_item_count()
        assert item_count == 0, (
            f"El carrito debería estar vacío, pero tiene {item_count} ítem(s)"
        )

        # Act - Volver a la tienda y agregar 2 productos
        cart.go_to_continue_shopping()
        inventory.add_two_to_cart()
        inventory.go_to_cart()

        # Assert - Verificar que hay 2 ítems
        cart_items = cart.get_cart_items()
        assert len(cart_items) == 2, (
            f"Se esperaban 2 ítems en el carrito, se encontraron {len(cart_items)}"
        )

        # Act - Checkout completo
        cart.go_to_checkout()
        checkout.fill_first_name("Belén")
        checkout.fill_last_name("García")
        checkout.fill_postal_code("7600")
        checkout.click_continue()
        checkout.click_finish()

        # Assert - Verificar compra exitosa
        confirmation = checkout.get_confirmation_header()
        assert "Thank you" in confirmation, (
            f"No se encontró mensaje de confirmación. Se obtuvo: '{confirmation}'"
        )
