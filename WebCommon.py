from appium import webdriver

echo_box_button_accessibility_id = "Login Screen"
echo_box_screen_field_accessibility_id = "messageInput"
app_path = "/Users/lukas/Desktop/boot-camp/theapp.apk"


class WebCommon:
    def __init__(self, apk_name):
        self.driver = None
        self.apk_name = apk_name
        self.desired_caps = {}
        self.init_driver()

    def init_driver(self):
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "deviceName": "R5CN81ML3VE",
            "automationName": "UiAutomator2",
            "app": self.apk_name,
            # "autoGrantPermissions": True
            "noReset": True
        }

    def get_driver(self):
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.desired_caps)
        return self.driver

    def close_driver(self):
        self.driver = self.get_driver().quit()


tescior01 = WebCommon(app_path).get_driver()
tescior01.find_element_by_accessibility_id(echo_box_button_accessibility_id).click()
tescior01.find_element_by_accessibility_id(echo_box_screen_field_accessibility_id).send_keys("Elo Andrei :)")
tescior01.implicitly_wait(2)
WebCommon(app_path).close_driver()
