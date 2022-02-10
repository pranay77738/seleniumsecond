from selenium.webdriver.common.by import By


class Confirmpage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    confirm_country = (By.LINK_TEXT, "India")
    ck_box = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR , "input[type='submit']")
    sucs_msg = (By.CLASS_NAME , "alert-success")

    def enter_country(self):
        return self.driver.find_element(*Confirmpage.country)

    def select_country(self):
        return self.driver.find_element(*Confirmpage.confirm_country)

    def select_chekbox(self):
        return self.driver.find_element(*Confirmpage.ck_box)

    def select_purchase(self):
        return self.driver.find_element(*Confirmpage.purchase)

    def get_message(self):
        return self.driver.find_element(*Confirmpage.sucs_msg)
