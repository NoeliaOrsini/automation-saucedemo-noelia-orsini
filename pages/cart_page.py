from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")

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