import pytest
from selenium import webdriver

driver = None


# passing web browser from command line
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")  # getting web browser name
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            "C:\\Users\\yjasw\\Downloads\\chromedriver_win32\\chromedriver.exe"
        )
    elif browser_name == "firefox":
        driver = webdriver.Firefox("")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "reports/" + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
