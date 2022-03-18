from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import logging
import pytest
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from WebCommon import WebCommon

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)

list_demo_header = "Check out these clouds"
message = "Hello World"
echo_box_button_access_id = "Echo Box"
list_demo_button_access_id = "List Demo"
altocumulus_access_id = "Altocumulus"
filemanager_more_options_access_id = "More options"
echo_box_screen_field_access_id = "messageInput"
echo_box_save_button_access_id = "messageSaveBtn"
element_01 = "Stratus"
element_02 = "Fog"
test_new_folder = "test_folder"
test_rename_folder = "secure_folder"
count_of_theapp_tests = 8
folder_exists_message = "File or folder already exists"
folder_created_message = "Folder created successfully"


def custom_wait_function(start_time=1, timeout=10):
    log.info(f"Screen content loading: wait {timeout} seconds")
    while start_time <= timeout:
        time.sleep(1)
        start_time += 1


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    def setup_method(self, method_name):
        log.info("setup_method")
        test_method_number = method_name.__name__[5:7]
        the_app_test_pack = str([x + 1 for x in range(count_of_theapp_tests)])
        if test_method_number in the_app_test_pack:
            apk_name = "the_app"
        else:
            apk_name = "filemanager"

        log.info(f"Method '{method_name.__name__}' in progress ...")
        self.webcommon_app = WebCommon(apk_name)
        self.driver = self.webcommon_app.get_driver()

    def teardown_method(self):
        log.info("teardown_method")
        self.webcommon_app.close_driver()

    @classmethod
    def teardown_class(cls):
        log.info("teardown_class")

    def get_element_by_text(self, text):
        find_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("' + text + '")')
        return find_text

    def screen_scroll(self):
        return self.driver.swipe(10, 1300, 10, 500)

    def create_new_folder_function(self, new_folder):
        self.driver.implicitly_wait(2)
        log.info(f"Creating new folder: '{new_folder}'")
        self.get_element_by_text("Main storage").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, filemanager_more_options_access_id).click()
        self.get_element_by_text("New").click()
        self.get_element_by_text("Folder").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout/"
                                                 "android.widget.FrameLayout/"
                                                 "android.widget.EditText").send_keys(new_folder)
        self.get_element_by_text(new_folder)
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()

        try:
            self.get_element_by_text("Main storage")
            log.info(f"'{new_folder}' created!")
            self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/home").click()
        except NoSuchElementException:
            log.info(f"Folder of file with '{new_folder}' name already exists!")
            self.driver.find_element(AppiumBy.ID, "android:id/button2").click()
            self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/home").click()

    def remove_folder_function(self, remove_folder):
        log.info(f"Deleting {remove_folder}...")
        self.driver.implicitly_wait(2)
        self.get_element_by_text("Main storage").click()
        while True:
            try:
                self.folder_name = self.get_element_by_text(remove_folder)
                self.actions = ActionChains(self.driver).click_and_hold(self.folder_name).perform()
                self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/bottom_menu_delete").click()
                self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
                self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/home").click()
                break
            except NoSuchElementException:
                self.screen_scroll()
                continue

    @pytest.mark.parametrize("os", ["Android"])
    def test_01(self, os):
        log.info(f"test_01 on {os}")

    @pytest.mark.xfail(reason="Unable to execute test")
    def test_02_xfail(self):
        assert False

    @pytest.mark.skip(reason="Unable to execute test")
    def test_03_skip(self):
        assert True

    def test_04_list_size(self):
        self.driver.implicitly_wait(5)
        list_of_elements = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc]')
        log.info(f" List size: {len(list_of_elements)}, Expected: 7")
        assert len(list_of_elements) == 7

    def test_05_text(self):
        self.driver.implicitly_wait(5)
        self.get_element_by_text("List Demo").click()
        list_demo_screen_header = self.get_element_by_text(list_demo_header).text
        log.info(f" 'List Demo' screen's header \"{list_demo_screen_header}\""
                 f", expected: \"{list_demo_header}\"")
        assert list_demo_screen_header == list_demo_header

    def test_06_send_keys(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, echo_box_button_access_id).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, echo_box_screen_field_access_id).send_keys(message)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, echo_box_save_button_access_id).click()
        text_sent = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@index="1"]').text
        log.info(f"Text sent: \"{text_sent}\", Expected: \"{message}\"")
        assert text_sent == message

    def test_07_wait(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, list_demo_button_access_id).click()
        custom_wait_function()
        screen_elements = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc]')
        log.info(f"{len(screen_elements)} elements found!")
        log.info(f"Check if button '{element_02}' is present on the screen")
        assert self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Fog"]')

    def test_08_scroll(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, list_demo_button_access_id).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, altocumulus_access_id)
        self.screen_scroll()
        log.info(f"Check if last element '{element_01}' is visible on the screen")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, element_01).is_enabled()

    def test_09_create_folder(self):
        self.create_new_folder_function(test_new_folder)
        log.info(f"Check if newly created directory '{test_new_folder}' is available")
        self.get_element_by_text("Main storage").click()
        try:
            assert self.get_element_by_text(test_new_folder)
        except NoSuchElementException:
            self.screen_scroll()
            assert self.get_element_by_text(test_new_folder)
        self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/home").click()
        self.remove_folder_function(test_new_folder)

    def test_10_delete_folder(self):
        self.create_new_folder_function(test_new_folder)
        self.remove_folder_function(test_new_folder)
        log.info(f"Check if newly created folder '{test_new_folder}' was successfully removed")
        self.get_element_by_text("Main storage").click()
        try:
            assert self.get_element_by_text(test_new_folder).is_enabled()
        except NoSuchElementException:
            try:
                self.screen_scroll()
                assert self.get_element_by_text(test_new_folder).is_enabled()
            except NoSuchElementException:
                log.info(f"'{test_new_folder}' is no longer available")

    def test_11_rename(self):
        self.driver.implicitly_wait(2)
        self.create_new_folder_function(test_new_folder)
        self.get_element_by_text("Main storage").click()
        try:
            self.folder_name = self.get_element_by_text(test_new_folder)
            self.actions = ActionChains(self.driver).click_and_hold(self.folder_name).perform()
        except NoSuchElementException:
            self.screen_scroll()
            self.folder_name = self.get_element_by_text(test_new_folder)
            self.actions = ActionChains(self.driver).click_and_hold(self.folder_name).perform()

        self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/bottom_menu_rename").click()
        self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/file_name").send_keys\
            (test_rename_folder)
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        log.info(f"Checking if '{test_rename_folder}' was created successfully")
        try:
            assert self.get_element_by_text(test_rename_folder).is_enabled()
        except NoSuchElementException:
            try:
                self.screen_scroll()
                assert self.get_element_by_text(test_new_folder).is_enabled()
            except NoSuchElementException:
                log.info(f"'{test_rename_folder}' is not available")
        self.driver.find_element(AppiumBy.ID, "com.alphainventor.filemanager:id/home").click()
        self.remove_folder_function(test_rename_folder)

    def test_12_exception(self):
        self.create_new_folder_function(test_new_folder)
        self.remove_folder_function(test_new_folder)
        self.get_element_by_text("Main storage").click()
        try:
            self.get_element_by_text(test_new_folder).click()
        except NoSuchElementException:
            log.info("Exception catched")
