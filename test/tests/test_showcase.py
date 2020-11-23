import warnings

import pytest


@pytest.fixture
def error():
    raise RuntimeError("intentional error")


def test_error(error):
    pass


def test_failing():
    assert False


@pytest.mark.xfail(reason="xfailed")
def test_xfail():
    assert False


@pytest.mark.xfail(reason="xfailed")
def test_xpassed():
    pass


@pytest.mark.skip(reason="skipped")
def test_skip():
    pass


def test_passing():
    pass


def test_warning():
    warnings.warn("warning", RuntimeWarning)
