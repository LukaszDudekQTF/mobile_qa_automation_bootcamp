import logging

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)


class Test01Android:
    def test_01(self):
        log.info("test_01")
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
