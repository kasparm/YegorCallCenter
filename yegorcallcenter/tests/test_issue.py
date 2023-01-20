import yegorcallcenter.Issue as Issue


def test_issue_init_resolution_status():
    i1 = Issue.Issue()
    assert i1._status == 0


def test_issue_post_resolution_status():
    i2 = Issue.Issue()
    i2.set_resolved()
    assert i2._status == 1
