import WebCommon
import logger_config

list_of_elements = WebCommon.driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc]')


def test_04_list_size():
    logger_config.log.info(f" List size: {len(list_of_elements)}, Expected: 7")
    assert len(list_of_elements) == 7
