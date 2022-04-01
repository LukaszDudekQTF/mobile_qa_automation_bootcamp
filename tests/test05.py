from WebCommon import WebCommon, the_app
from utils import logger_config

list_demo_header = "Check out these clouds"
driver = WebCommon(the_app).get_driver()


def get_element_by_text(text):
    find_text = driver.find_element_by_android_uiautomator('new UiSelector().text("' + text + '")')
    return find_text


def test_05_text():
    # to open LIST DEMO I needed to look for "Photo Demo" string because this value matches "List Demo" button in app
    get_element_by_text("Photo Demo").click()
    list_demo_screen_header = get_element_by_text(list_demo_header).text
    logger_config.log.info(f" 'List Demo' screen's header \"{list_demo_screen_header}\", \
    expected: \"{list_demo_header}\"")
    assert list_demo_screen_header == list_demo_header
