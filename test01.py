import logging
import pytest

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)


class Test01Android:
    @pytest.mark.parametrize("os", ["Android"])
    def test_01(self, os):
        log.info("test_01")
        log.info("Android")
        assert True

    def setup_method(self, method):
        log.info("setup_method")
        pass

    @classmethod
    def setup_class(cls):
        log.info("setup_class")
        pass

    @classmethod
    def teardown_class(cls):
        log.info("teardown_class")
        pass

    def teardown_method(self, method):
        log.info("teardown_method")
        pass
