def hacer_click(driver, elemento):
    """Hace click en un elemento usando JavaScript"""
    driver.execute_script("arguments[0].click();", elemento)


def escribir(driver, elemento, texto):
    """
    Escribe 'texto' en un campo de un formulario.
    """
    driver.execute_script(
        "const campo = arguments[0], valor = arguments[1];"
        "const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;"
        "setter.call(campo, valor);"
        "campo.dispatchEvent(new Event('input', { bubbles: true }));",
        elemento, texto,
    )
