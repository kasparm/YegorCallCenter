import pytest

import yegorcallcenter.CallCenter as CC
import yegorcallcenter.Call

def test_callcenter_creation():
    call_center = CC.CallCenter()
    assert  not call_center._activecalls
    assert not call_center._employee
    assert not call_center._queue

    call_center1 = CC.CallCenter(10,2,1)
    assert len(call_center1._employee) == 13

def test_callcenter_new_call():
    call_center = CC.CallCenter(10,2,1)


def test_callcenter_overload():
    assert True

def test_callcenter_escalation():
    assert True

