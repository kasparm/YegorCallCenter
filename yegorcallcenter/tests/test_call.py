import pytest

import yegorcallcenter.Call as call
import yegorcallcenter.Caller as caller
import yegorcallcenter.Issue as issue

def test_call():
    cler = caller.Caller('test')
    iue = issue.Issue()
    c = call.Call(cler, iue)
    assert c._in_progress
