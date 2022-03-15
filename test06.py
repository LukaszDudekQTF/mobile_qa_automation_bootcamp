import logger_config
from WebCommon import WebCommon, the_app
from appium.webdriver.common.touch_action import TouchAction


message = "Hello World"
echo_box_button_accessibility_id = "Login Screen"
echo_box_screen_field_accessibility_id = "messageInput"
echo_box_save_button_accessibility_id = "messageSaveBtn"

driver = WebCommon(the_app).get_driver()


def test_06_send_keys():
    driver.find_element_by_accessibility_id(echo_box_button_accessibility_id).click()
    driver.implicitly_wait(1)
    driver.find_element_by_accessibility_id(echo_box_screen_field_accessibility_id).send_keys(message)
    # driver.find_element_by_accessibility_id(echo_box_save_button_accessibility_id).click()
    driver.implicitly_wait(1)
    TouchAction(driver).tap(x=543, y=1414).perform()
    text_sent = driver.find_element_by_xpath('//android.widget.TextView[@index="1"]').text
    logger_config.log.info(f"Text sent: \"{text_sent}\", Expected: \"{message}\"")
    assert text_sent == message
