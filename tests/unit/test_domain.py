import pytest

from link_shortener.domain.codes import Codes
from link_shortener.domain.link import Link


def test_link_construction():
    link = Link(1, "www.test.com")
    assert link.link_id == 1
    assert link.url == "www.test.com"
    assert link.updated_link is None


def test_link_changed():
    link = Link(1, "www.test.com")
    link.update_link("www.updatedlink")
    assert link.updated_link == "www.updatedlink"


def test_generates_codes(new_code):
    assert new_code.generated_code is None
    new_code.generate_code()
    assert new_code.generated_code is not None
    assert new_code.original_url.url == "www.test.com"


def test_codes_rejects_non_link_values():
    with pytest.raises(TypeError):
        Codes("www.test.com")