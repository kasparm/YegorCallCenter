import yegorcallcenter.Call as Call
import yegorcallcenter.Caller as Caller
import yegorcallcenter.Employee as Employee
import yegorcallcenter.Issue as Issue


def test_call():
    cler = Caller.BasicCaller("test")
    iue = Issue.BasicIssue()
    c = Call.BasicCall(cler, iue)
    assert c._call_status.in_progress()


def test_call_assignment():
    cler = Caller.BasicCaller("test")
    iue = Issue.BasicIssue()
    iue._difficulty = 0
    c = Call.BasicCall(cler, iue)
    resolved = c.resolved(Employee.Operator(name="tester", skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.resolved(Employee.Operator(name="tester", skill=1))
    assert not resolved
    iue._difficulty = 2
    resolved = c.resolved(Employee.Operator(name="tester", skill=1))
    assert not resolved

    iue._difficulty = 0
    resolved = c.resolved(Employee.Supervisor(name="tester", skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.resolved(Employee.Supervisor(name="tester", skill=1))
    assert resolved
    iue._difficulty = 2
    resolved = c.resolved(Employee.Supervisor(name="tester", skill=1))
    assert not resolved

    iue._difficulty = 0
    resolved = c.resolved(Employee.Director(name="tester", skill=1))
    assert resolved
    iue._difficulty = 1
    resolved = c.resolved(Employee.Director(name="tester", skill=1))
    assert resolved
    iue._difficulty = 2
    resolved = c.resolved(Employee.Director(name="tester", skill=1))
    assert resolved
