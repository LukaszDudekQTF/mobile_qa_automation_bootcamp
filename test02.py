
import pytest


@pytest.mark.xfail(reason="Unable to execute test")
def test_02_xfail():
    assert False
