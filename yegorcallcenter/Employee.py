import uuid
from abc import ABCMeta

from yegorcallcenter.EmployeeQualification import EmployeeQualification


class Employee(metaclass=ABCMeta):
    def __init__(self, name=None, level=0, skill=0) -> None:
        """Employee of the call center

        Args:
            id (int): ID of the employee
            name (string): name of the employee, default is id
            level (int): level of the employee 0 = operator, 1 = supervisor, 2 = director
            skill (int): skill of the employee 0 = not very, 1 = skilled, 2 = very skilled
        """
        self._id = uuid.uuid4()
        self._name = name if name else self._id
        self._qualification = EmployeeQualification(level, skill)
        self._busy = False

    def get_name(self):
        return self._name

    def get_qualification(self):
        return self._qualification

    def set_busy(self):
        self._busy = True

    def set_free(self):
        self._busy = False

    def is_busy(self):
        return self._busy


class Operator(Employee):
    def __init__(self, name=uuid.uuid4(), level=0, skill=1) -> None:
        super().__init__(name, level, skill)


class Supervisor(Employee):
    def __init__(self, name=uuid.uuid4(), level=1, skill=1) -> None:
        super().__init__(name, level, skill)


class Director(Employee):
    def __init__(self, name=uuid.uuid4(), level=2, skill=1) -> None:
        super().__init__(name, level, skill)
