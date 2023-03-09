from yegorcallcenter import Employee as Employee


def test_employee_operator():
    a = Employee.Operator("toor")
    assert a.get_name() == "toor"
