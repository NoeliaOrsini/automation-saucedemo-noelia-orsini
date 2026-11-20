from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators catálogo y carrito
        self.add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        
        # Nuevos Locators para el flujo de Checkout
        self.checkout_button = (By.ID, "checkout")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")
        
    def agregar_backpack_al_carrito(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.add_to_cart_backpack))
        boton.click()
        

    def obtener_numero_badge(self):
        badge = self.wait.until(EC.presence_of_element_located(self.cart_badge))
        return badge.text

    def ir_al_carrito(self):
        icono = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        icono.click()
        self.wait.until(EC.url_contains("/cart.html"))

    def obtener_nombre_item(self):
        return self.wait.until(EC.presence_of_element_located(self.item_name)).text

    def obtener_precio_item(self):
        return self.wait.until(EC.presence_of_element_located(self.item_price)).text
    
    # Métodos nuevos para el Checkout
    def ir_al_checkout(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        # Scroll preventivo y validación de URL para evitar timeouts en modo headless (CI)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton) 
        boton.click()
        self.wait.until(EC.url_contains("/checkout-step-one.html")) 

    def completar_datos_envio(self, nombre, apellido, codigo_postal):
        # Espera, enfoca y completa cada campo para asegurar que React registre los valores en CI
        first_name = self.wait.until(EC.element_to_be_clickable(self.first_name_input))
        first_name.click()
        first_name.clear()
        first_name.send_keys(nombre)

        last_name = self.wait.until(EC.element_to_be_clickable(self.last_name_input))
        last_name.click()
        last_name.clear()
        last_name.send_keys(apellido)

        postal_code = self.wait.until(EC.element_to_be_clickable(self.postal_code_input))
        postal_code.click()
        postal_code.clear()
        postal_code.send_keys(codigo_postal)

        # Centra el botón Continue, ejecuta el clic por JS y verifica el avance al resumen
        btn_continuar = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_continuar)
        self.driver.execute_script("arguments[0].click();", btn_continuar)
        self.wait.until(EC.url_contains("/checkout-step-two.html"))
        
    def finalizar_compra(self):
        btn_finish = self.wait.until(EC.element_to_be_clickable(self.finish_button))
        # Centra el botón Finish en el viewport de CI antes de confirmar la compra
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_finish) 
        btn_finish.click()
        self.wait.until(EC.url_contains("/checkout-complete.html")) 

    def obtener_mensaje_exito(self):
        mensaje = self.wait.until(EC.presence_of_element_located(self.success_message))
        return mensaje.text