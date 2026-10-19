import pytest
from link_shortener.domain.link import Link
from link_shortener.domain.codes import Codes

@pytest.fixture
def new_link(): 
    return Link(1, "www.test.com")

@pytest.fixture
def new_code():
    return Codes(Link(1, "www.test.com"))