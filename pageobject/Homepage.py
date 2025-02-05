from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobject.Shoppage import Shoppage


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.XPATH, "//input[@class='form-control']")
    checkbox = (By.CSS_SELECTOR, "input[class='form-check-input']")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radiobtn = (By.ID, "inlineRadio2")
    bdy = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@value='Submit']")
    msg = (By.CLASS_NAME, "alert-success")
    shp = (By.LINK_TEXT, "Shop")

    def get_name(self):
        return self.driver.find_element(*Homepage.name)

    def get_email(self):
        return self.driver.find_element(*Homepage.email)

    def get_password(self):
        return self.driver.find_element(*Homepage.password)

    def get_checkbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def get_dropdown(self):
        return self.driver.find_element(*Homepage.dropdown)

    def get_radiobtn(self):
        return self.driver.find_element(*Homepage.radiobtn)

    def get_bday(self):
        return self.driver.find_element(*Homepage.bdy)

    def get_submit(self):
        return self.driver.find_element(*Homepage.submit)

    def get_msg(self):
        return self.driver.find_element(*Homepage.msg)

    def get_shop(self):
        self.driver.find_element(*Homepage.shp).click()
        shoppage = Shoppage(self.driver)
        return shoppage
