from selenium.webdriver.common.by import By

from pageobject.Checkoutpage import Checkoutpage


class Shoppage:
    def __init__(self, driver):
        self.driver = driver

    shp_items = (By.CSS_SELECTOR, ".card-title a")
    clk_items = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkout = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def get_shopitems2(self):
        return self.driver.find_elements(*Shoppage.shp_items)

    def get_clickitem(self):
        return self.driver.find_element(*Shoppage.clk_items)

    def get_checkout(self):
        self.driver.find_element(*Shoppage.checkout).click()
        checkoutpage = Checkoutpage(self.driver)
        return checkoutpage
