import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.logger import logger

@pytest.mark.checkout
def test_checkout_completo(driver):
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)

    try:
        logger.info("Iniciando prueba de flujo completo de Checkout")

        # 1. Login previo
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso previo al checkout")

        # 2. Agregar producto y entrar al carrito
        cart_page.agregar_backpack_al_carrito()
        cart_page.ir_al_carrito()
        logger.info("Producto agregado y usuario posicionado en el carrito")

        # 3. Iniciar el checkout
        cart_page.ir_al_checkout()
        assert "/checkout-step-one.html" in driver.current_url
        logger.info("Transición a la pantalla de datos de envío exitosa")

        # 4. Completar formulario de envío
        cart_page.completar_datos_envio("Noelia", "Orsini", "7240")
        logger.info("Datos de envío completados (Nombre, Apellido y Código Postal)")

        # 5. Finalizar compra
        cart_page.finalizar_compra()
        assert "/checkout-complete.html" in driver.current_url
        logger.info("Resumen de compra aprobado y botón 'Finish' presionado")

        # 6. Validar mensaje de éxito
        mensaje = cart_page.obtener_mensaje_exito()
        assert mensaje == "Thank you for your order!"
        logger.info(f"¡Checkout finalizado con éxito! Mensaje verificado: '{mensaje}'")

    except Exception:
        logger.exception("Error crítico durante la ejecución de la prueba de Checkout")
        raise