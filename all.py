from appium import webdriver
import logging
import pytest

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)

the_app = "/Users/lukas/Desktop/boot-camp/theapp.apk"


class WebCommon:
    def __init__(self, apk_name):
        self.driver = None
        self.init_driver(apk_name)
        # self.get_driver()

    def init_driver(self, apk_name):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "deviceName": "R5CN81ML3VE",
            "automationName": "UiAutomator2",
            "app": apk_name,
            # "autoGrantPermissions": True
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    def setup_method(self, method):
        log.info("setup_method")

    @pytest.mark.parametrize("os", ["Android"])
    def test_01(self, os):
        log.info(f"test_01 on {os}")

    def teardown_method(self, method):
        log.info("teardown_method")

    @classmethod
    def teardown_class(cls):
        log.info("teardown_class")