import logging

log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)


class Test01Android:
    def test_01(self):
        log.info("test_01")
        assert True
