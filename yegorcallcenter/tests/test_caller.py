import yegorcallcenter.Caller as Caller


def test_caller_creation():
    a1 = Caller.Caller("curt")
    assert a1._name == "curt"
