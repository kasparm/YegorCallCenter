import abc


class EmployeeQualification(metaclass=abc.ABCMeta):
    def __init__(self, level=0, skill=0) -> None:
        pass

    @abc.abstractclassmethod
    def level(self):
        return self._level

    @abc.abstractclassmethod
    def skill(self):
        return self._skill


class BasicEmployeeQualification(EmployeeQualification):
    def __init__(self, level=0, skill=0) -> None:
        super().__init__()
        self._level = level
        self._skill = skill

    def level(self):
        return self._level

    def skill(self):
        return self._skill
