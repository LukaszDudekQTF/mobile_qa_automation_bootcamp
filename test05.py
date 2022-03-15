import WebCommon

list_demo_header = "Check out these clouds"


def get_element_by_text(text):
    find_text = WebCommon.driver.find_element_by_android_uiautomator('new UiSelector().text("' + text + '")')
    return find_text


def test_05_text():
    # to open LIST DEMO I needed to look for "Photo Demo" string because this value matches "List Demo" button in app
    get_element_by_text("Photo Demo").click()
    assert get_element_by_text(list_demo_header).text == "Check out these clouds"
