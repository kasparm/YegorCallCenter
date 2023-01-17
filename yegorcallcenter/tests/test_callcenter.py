import pytest

import yegorcallcenter.CallCenter as CC
import yegorcallcenter.Call as Call
import yegorcallcenter.Issue as Issue
import yegorcallcenter.Caller as Caller

def test_callcenter_creation():
    call_center = CC.CallCenter()
    assert not call_center._activecalls
    assert not call_center._queue

    call_center1 = CC.CallCenter(10,2,1)
    assert len(call_center1._employee[0]) + len(call_center1._employee[1]) + len(call_center1._employee[2]) == 13


def test_callcenter_new_call():
    call_center = CC.CallCenter(10,2,1)
    
    caller_01 = Caller.Caller("testter_01")
    issue_01 = Issue.Issue()
    call_01 = Call.Call(caller_01,issue_01)

    call_center.incomming_call(call_01)
    call_center.incomming_call(call_01)

    issue_02 = Issue.Issue()
    issue_02._difficulty = 2
    call_02 = Call.Call(caller_01,issue_02)
    assert call_02.get_issue().get_status() == 0
    assert call_02.get_escal_level() == 0
    call_center.incomming_call(call_02)
    assert call_02.get_escal_level() == 2
    assert call_02.get_issue().get_status() == 1
    assert call_02.get_escal_level() == 2

def test_callcenter_escalation():
    call_center = CC.CallCenter(1,1,1)
    difficulty = [1,2]
    for i in range(len(difficulty)):
        caller_01 = Caller.Caller("testter_01")
        issue_01 = Issue.Issue()
        issue_01._difficulty = difficulty[i]
        call_01 = Call.Call(caller_01,issue_01)
        call_center.incomming_call(call_01)

def test_callcenter_overload():
    call_center = CC.CallCenter(1,1,1)
    difficulty = 2
    n_calls = 10
    for i in range(n_calls):
        caller_01 = Caller.Caller("testter_01")
        issue_01 = Issue.Issue()
        issue_01._difficulty = difficulty
        call_01 = Call.Call(caller_01,issue_01)
        call_center.incomming_call(call_01)

