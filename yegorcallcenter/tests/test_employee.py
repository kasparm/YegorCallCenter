from yegorcallcenter import Employee as Employee


def test_employee_operator():
    a = Employee.Operator("toor")
    assert a.get_level() == 0
    assert a.get_name() == "toor"


def test_employee_supervisor():
    b = Employee.Supervisor("toor")
    assert b.get_level() == 1


def test_employee_director():
    c = Employee.Director("toor")
    assert c.get_level() == 2


def test_employee_01():
    a = Employee.Operator()
    assert a.get_level() == 0
