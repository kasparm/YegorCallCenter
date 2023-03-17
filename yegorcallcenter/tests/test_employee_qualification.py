import pytest

from yegorcallcenter.EmployeeQualification import BasicEmployeeQualification


@pytest.fixture
def qualification():
    return BasicEmployeeQualification(level=5, skill=8)


def test_get_level(qualification):
    assert qualification.level() == 5


def test_get_skill(qualification):
    assert qualification.skill() == 8


def test_default_values():
    qualification = BasicEmployeeQualification()
    assert qualification.level() == 0
    assert qualification.skill() == 0
