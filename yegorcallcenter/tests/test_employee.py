from yegorcallcenter import Employee as Employee


def test_employee_operator():
    a = Employee.Operator("toor")
    assert a.get_name() == "toor"


def test_employee_level():
    a = Employee.Supervisor()
    assert a.get_qualification().get_level() == 1
