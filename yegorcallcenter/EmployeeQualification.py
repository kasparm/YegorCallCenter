import abc


class EmployeeQualification(metaclass=abc.ABCMeta):
    def __init__(self, level=0, skill=0) -> None:
        pass

    @abc.abstractclassmethod
    def get_level(self):
        return self._level

    @abc.abstractclassmethod
    def get_skill(self):
        return self._skill


class BasicEmployeeQualification(EmployeeQualification):
    def __init__(self, level=0, skill=0) -> None:
        super().__init__()
        self._level = level
        self._skill = skill

    def get_level(self):
        return self._level

    def get_skill(self):
        return self._skill
