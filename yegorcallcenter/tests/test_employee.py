from yegorcallcenter import Employee as Employee


def test_employee_operator():
    a = Employee.Operator("toor")
    assert a.name() == "toor"


def test_employee_level():
    a = Employee.Supervisor()
    assert a.qualification().level() == 1
