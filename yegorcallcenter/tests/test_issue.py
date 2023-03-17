import yegorcallcenter.Issue as Issue


def test_issue_init_resolution_status():
    i1 = Issue.BasicIssue()
    assert i1._status == 0


def test_issue_post_resolution_status():
    i2 = Issue.BasicIssue()
    i2.resolve()
    assert i2._status == 1
