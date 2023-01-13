import pytest

import yegorcallcenter.Call as call
import yegorcallcenter.Caller as caller
import yegorcallcenter.Issue as issue
import yegorcallcenter.Employee as empl

def test_call():
    cler = caller.Caller('test')
    iue = issue.Issue()
    c = call.Call(cler, iue)
    assert c._in_progress

def test_call_assignement():
    cler = caller.Caller('test')
    iue = issue.Issue()
    iue._difficulty = 0
    c = call.Call(cler, iue)
    resolved = c.assign_employee(empl.Employee(name='tester',level=0,skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.assign_employee(empl.Employee(name='tester',level=0,skill=1))
    assert resolved == False
    iue._difficulty = 2
    resolved = c.assign_employee(empl.Employee(name='tester',level=0,skill=1))
    assert resolved == False
    
    iue._difficulty = 0
    resolved = c.assign_employee(empl.Employee(name='tester',level=1,skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.assign_employee(empl.Employee(name='tester',level=1,skill=1))
    assert resolved
    iue._difficulty = 2
    resolved = c.assign_employee(empl.Employee(name='tester',level=1,skill=1))
    assert resolved == False

    iue._difficulty = 0
    resolved = c.assign_employee(empl.Employee(name='tester',level=2,skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.assign_employee(empl.Employee(name='tester',level=2,skill=1))
    assert resolved
    iue._difficulty = 2
    resolved = c.assign_employee(empl.Employee(name='tester',level=2,skill=1))
    assert resolved

