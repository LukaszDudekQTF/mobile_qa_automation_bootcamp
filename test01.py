import logging

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)


class Test01Android:
    def test_01(self):
        log.info("test_01")
        assert True

    @classmethod
    def setup_class(cls):
        # set up some state
        log.info("setup_class")
        pass

    @classmethod
    def teardown_class(cls):
        # teardown state
        log.info("teardown_class")
        pass
