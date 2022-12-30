import pytest

from yegorcallcenter import Employee as emp

def test_employee_operator():
    a = emp.Operator('toor')
    assert a.level == 0
    assert a.name =="toor"

def test_employee_supervisor():
    b = emp.Supervisor('toor')
    assert b.level == 1

def test_employee_director():
    c = emp.Director('toor')
    assert c.level == 2

def test_employee_01():
    a = emp.Operator()
    assert a.level == 0
