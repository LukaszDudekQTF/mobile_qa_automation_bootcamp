from appium import webdriver


# MAC localizations
# the_app = "/Users/lukas/Desktop/boot-camp/theapp.apk"
# filemanager = "/Users/lukas/Desktop/boot-camp/filemanager.apk"

# Windows localizations
# the_app = "C:\\Users\\lukas\\Desktop\\mobile_qa_automation_bootcamp\\theapp.apk"
# filemanager = "C:\\Users\\lukas\\Desktop\\mobile_qa_automation_bootcamp\\filemanager.apk"

# GitHub localization
# the_app = "//apps/theapp.apk"
# filemanager = "//apps/filemanager.apk"

# Linux localization
the_app = "/home/lukas/PycharmProjects/mobile_qa_automation_bootcamp/apps/theapp.apk"
filemanager = "/home/lukas/PycharmProjects/mobile_qa_automation_bootcamp/apps/filemanager.apk"


class WebCommon:
    def __init__(self, apk_name):
        self.driver = None
        self.init_driver(apk_name)

    def init_driver(self, apk_name):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "emulator-5554",
            # "automationName": "UiAutomator2",
            "autoGrantPermissions": True
            # "noReset": True
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
