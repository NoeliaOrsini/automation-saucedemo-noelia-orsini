from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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

    def obtener_nombre_item(self):
        return self.wait.until(EC.presence_of_element_located(self.item_name)).text

    def obtener_precio_item(self):
        return self.wait.until(EC.presence_of_element_located(self.item_price)).text
    
    # Métodos nuevos para el Checkout
    def ir_al_checkout(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        boton.click()

    def completar_datos_envio(self, nombre, apellido, codigo_postal):
        self.wait.until(EC.presence_of_element_located(self.first_name_input)).send_keys(nombre)
        self.driver.find_element(*self.last_name_input).send_keys(apellido)
        self.driver.find_element(*self.postal_code_input).send_keys(codigo_postal)
        
        btn_continuar = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        btn_continuar.click()

    def finalizar_compra(self):
        btn_finish = self.wait.until(EC.element_to_be_clickable(self.finish_button))
        btn_finish.click()

    def obtener_mensaje_exito(self):
        mensaje = self.wait.until(EC.presence_of_element_located(self.success_message))
        return mensaje.text