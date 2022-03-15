import logging
import pytest

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    def setup_method(self, method):
        log.info("setup_method")

    @pytest.mark.parametrize("os", ["Android"])
    def test_01(self, os):
        log.info(f"test_01 on {os}")

    def teardown_method(self, method):
        log.info("teardown_method")

    @classmethod
    def teardown_class(cls):
        log.info("teardown_class")
