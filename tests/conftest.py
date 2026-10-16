import pytest
from link_shortener.domain.link import Link

@pytest.fixture
def new_link(): 
    return Link(1, "www.test.com")

