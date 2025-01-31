from selenium.webdriver.common.by import By

from pageobject.Confirmpage import Confirmpage


class Checkoutpage:
    def __init__(self, driver):
        self.driver = driver

    cart_items = (By.XPATH, "//table[@class='table table-hover']/tbody/tr/td/div/div/h4")
    confirm_checkout = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    # Pranay kumar

    def get_cartiems(self):
        return self.driver.find_elements(*Checkoutpage.cart_items)

    def get_confirmcheckout(self):
        self.driver.find_element(*Checkoutpage.confirm_checkout).click()
        confirmpage = Confirmpage(self.driver)
        return confirmpage
