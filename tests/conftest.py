import pytest


@pytest.fixture
def raw_input():
    return "0 0 0 0 0 0 0 0 0\n0 1 0 0 0 0 0 0 0\n1 1 1 0 0 0 1 0 0\n1 1 0 0 0 1 1 1 0\n0 0 0 0 0 1 1 0 0\n0 0 1 0 0 0 0 0 0\n1 1 0 0 0 0 0 0 0\n0 0 0 0 0 1 1 0 0\n"
