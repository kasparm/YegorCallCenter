import abc
import uuid

from yegorcallcenter.EmployeeQualification import BasicEmployeeQualification


class Employee(metaclass=abc.ABCMeta):
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
        self._qualification = BasicEmployeeQualification(level, skill)
        self._busy = False

    @abc.abstractmethod
    def name(self):
        raise NotImplementedError

    @abc.abstractmethod
    def qualification(self):
        raise NotImplementedError

    @abc.abstractmethod
    def assign(self):
        raise NotImplementedError

    @abc.abstractmethod
    def release(self):
        raise NotImplementedError

    @abc.abstractmethod
    def busy(self):
        raise NotImplementedError


class Operator(Employee):
    def __init__(self, name=uuid.uuid4(), skill=1) -> None:
        super().__init__(name, level=0, skill=skill)

    def name(self):
        return self._name

    def qualification(self):
        return self._qualification

    def assign(self):
        self._busy = True

    def release(self):
        self._busy = False

    def busy(self):
        return self._busy


class Supervisor(Employee):
    def __init__(self, name=uuid.uuid4(), skill=1) -> None:
        super().__init__(name, level=1, skill=skill)

    def name(self):
        return self._name

    def qualification(self):
        return self._qualification

    def assign(self):
        self._busy = True

    def release(self):
        self._busy = False

    def busy(self):
        return self._busy


class Director(Employee):
    def __init__(self, name=uuid.uuid4(), skill=1) -> None:
        super().__init__(name, level=2, skill=skill)

    def name(self):
        return self._name

    def qualification(self):
        return self._qualification

    def assign(self):
        self._busy = True

    def release(self):
        self._busy = False

    def busy(self):
        return self._busy
