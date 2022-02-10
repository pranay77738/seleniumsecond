import pytest
from TestData.Homepagedata import HomePageData
from pageobject.Homepage import Homepage
from utilities.Baseclass import Baseclass


class TestHomepage(Baseclass):

    def test_homepage(self, getData):

        log = self.test_logging()
        homepage = Homepage(self.driver)
        log.info("Name is "+getData["name"])
        log.info("Email is "+getData["email"])
        log.info("Password is "+getData["password"])
        homepage.get_name().send_keys(getData["name"])
        homepage.get_email().send_keys(getData["email"])
        homepage.get_password().send_keys(getData["password"])
        homepage.get_checkbox().click()

        # dropdown = Select(homepage.get_dropdown())
        # dropdown.select_by_visible_text("Female")
        self.selectoptionbytest(homepage.get_dropdown(),"Female")

        homepage.get_radiobtn().click()

        homepage.get_bday().send_keys("03/02/1997")

        homepage.get_submit().click()

        message = homepage.get_msg().text
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.homepage_test_data)
    def getData(self,request):
        return request.param
