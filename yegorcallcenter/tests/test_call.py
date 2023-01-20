import yegorcallcenter.Call as Call
import yegorcallcenter.Caller as Caller
import yegorcallcenter.Employee as Employee
import yegorcallcenter.Issue as Issue


def test_call():
    cler = Caller.Caller("test")
    iue = Issue.Issue()
    c = Call.Call(cler, iue)
    assert c._in_progress


def test_call_assignement():
    cler = Caller.Caller("test")
    iue = Issue.Issue()
    iue._difficulty = 0
    c = Call.Call(cler, iue)
    resolved = c.assign_employee(Employee.Employee(name="tester", level=0, skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.assign_employee(Employee.Employee(name="tester", level=0, skill=1))
    assert not resolved
    iue._difficulty = 2
    resolved = c.assign_employee(Employee.Employee(name="tester", level=0, skill=1))
    assert not resolved

    iue._difficulty = 0
    resolved = c.assign_employee(Employee.Employee(name="tester", level=1, skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.assign_employee(Employee.Employee(name="tester", level=1, skill=1))
    assert resolved
    iue._difficulty = 2
    resolved = c.assign_employee(Employee.Employee(name="tester", level=1, skill=1))
    assert not resolved

    iue._difficulty = 0
    resolved = c.assign_employee(Employee.Employee(name="tester", level=2, skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.assign_employee(Employee.Employee(name="tester", level=2, skill=1))
    assert resolved
    iue._difficulty = 2
    resolved = c.assign_employee(Employee.Employee(name="tester", level=2, skill=1))
    assert resolved
