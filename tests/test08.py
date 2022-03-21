import logger_config
from WebCommon import WebCommon, the_app

driver = WebCommon(the_app).get_driver()
element = "Stratus"


def screen_scroll():
    return driver.swipe(500, 2100, 500, 1100, 1000)


def test_08_scroll():
    driver.implicitly_wait(5)
    driver.find_element_by_accessibility_id("Photo Demo").click()
    driver.find_element_by_accessibility_id("Altocumulus")
    screen_scroll()
    logger_config.log.info(f"Check if {element} is visible on the screen")
    assert driver.find_element_by_accessibility_id(element).is_enabled()
