import pytest

from yegorcallcenter.EmployeeQualification import EmployeeQualification


@pytest.fixture
def qualification():
    return EmployeeQualification(level=5, skill=8)


def test_get_level(qualification):
    assert qualification.get_level() == 5


def test_get_skill(qualification):
    assert qualification.get_skill() == 8


def test_default_values():
    qualification = EmployeeQualification()
    assert qualification.get_level() == 0
    assert qualification.get_skill() == 0
