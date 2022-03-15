from appium import webdriver

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
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
