import yegorcallcenter.Caller as Caller


def test_caller_creation():
    a1 = Caller.Caller("curt")
    assert a1._name == "curt"
    
def test_caller_creation2():
    a2 = Caller.Caller()
    assert a2._name == a2._id
