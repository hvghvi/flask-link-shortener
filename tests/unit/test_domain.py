def test_link_construction(new_link):
    assert new_link.link_id == 1
    assert new_link.url == "www.test.com"
    assert new_link.updated_link is None

def test_link_changed(new_link):
    assert new_link.url == "www.test.com"
    new_link.update_link("www.updatedlink")
    assert new_link.updated_link == "www.updatedlink"