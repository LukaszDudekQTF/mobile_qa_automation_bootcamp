from utils import logger_config
from WebCommon import WebCommon, the_app
import time

driver = WebCommon(the_app).get_driver()


def wait(start_time=1, timeout=10):
    logger_config.log.info(f"Screen content loading: wait {timeout} seconds")
    while start_time <= timeout:
        time.sleep(1)
        start_time += 1


def test_07_wait():
    driver.find_element_by_accessibility_id("Photo Demo").click()
    wait()
    screen_elements = driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc]')
    logger_config.log.info(f"{len(screen_elements)} elements found!")
    driver.implicitly_wait(12)
    logger_config.log.info("Check if button 'FOG' is present on the screen")
    assert driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc="Fog"]')
