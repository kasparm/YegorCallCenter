import pytest

from yegorcallcenter import Employee as emp

def test_employee_operator():
    a = emp.Operator('toor')
    assert a.get_level() == 0
    assert a.get_name() =="toor"

def test_employee_supervisor():
    b = emp.Supervisor('toor')
    assert b.get_level() == 1

def test_employee_director():
    c = emp.Director('toor')
    assert c.get_level() == 2

def test_employee_01():
    a = emp.Operator()
    assert a.get_level() == 0
