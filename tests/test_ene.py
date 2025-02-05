import time
from pageobject.Homepage import Homepage
from utilities.Baseclass import Baseclass


# @pytest.mark.usefixtures("setup")
class TestEndtoEnd(Baseclass):
    def test_ene(self):
        log = self.test_logging()
        homepage = Homepage(self.driver)
        self.driver.refresh()
        # driver.find_element(By.XPATH,"//*[contains(text(), 'Name is required')]").text
        shoppage = homepage.get_shop()
        log.info("getting all the card titles")

        # using javascript to click the button without using selenium
        # self.driver.execute_script("arguments[0].click();", dd)
        time.sleep(1)
        # shoppage = Shoppage(self.driver)
        elements = shoppage.get_shopitems2()
        i = -1
        for element in elements:
            log.info(element.text)
            i += 1
            # prod = element.find_element(By.XPATH, "div/h4/a").text
            if element.text == "iphone X":
                shoppage.get_clickitem().click()

        checkoutpage = shoppage.get_checkout()
        # checkoutpage = Checkoutpage(self.driver)

        items = checkoutpage.get_cartiems()

        confirmpage = checkoutpage.get_confirmcheckout()

        # confirmpage = Confirmpage(self.driver)
        log.info("entering country name as ind")
        confirmpage.enter_country().send_keys("ind")
        self.verifytextpresent("India")
        confirmpage.select_country().click()
        confirmpage.select_chekbox().click()
        confirmpage.select_purchase().click()
        mess = confirmpage.get_message().text
        log.info("text received from the browser" + mess)
        assert "Success" in mess
        # driver.get_screenshot_as_file("scren.png")
