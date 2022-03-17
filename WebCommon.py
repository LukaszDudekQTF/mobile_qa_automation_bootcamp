from appium import webdriver

the_app = "/Users/lukas/Desktop/boot-camp/theapp.apk"
filemanager = "/Users/lukas/Desktop/boot-camp/filemanager.apk"


class WebCommon:
    def __init__(self, apk_name):
        self.driver = None
        self.init_driver(apk_name)

    def init_driver(self, apk_name):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "deviceName": "R5CN81ML3VE",
            "automationName": "UiAutomator2",
            # "autoGrantPermissions": True
            "noReset": True
        }

        if apk_name == "the_app":
            desired_caps["app"] = the_app
        elif apk_name == "filemanager":
            desired_caps["app"] = filemanager

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
