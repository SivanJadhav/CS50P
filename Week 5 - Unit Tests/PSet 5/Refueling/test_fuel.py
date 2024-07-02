import pytest
from fuel import convert, gauge


def testing_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67

    # Testing for Exceptions
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


def testing_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")


def testing_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
