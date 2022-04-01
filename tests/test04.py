from WebCommon import WebCommon, the_app
from utils import logger_config

driver = WebCommon(the_app).get_driver()


def test_04_list_size():
    list_of_elements = driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc]')
    driver.implicitly_wait(1)
    logger_config.log.info(f" List size: {len(list_of_elements)}, Expected: 7")
    assert len(list_of_elements) == 7
