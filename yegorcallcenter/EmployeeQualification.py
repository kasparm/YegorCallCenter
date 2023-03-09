class EmployeeQualification:
    def __init__(self, level=0, skill=0) -> None:
        self._level = level
        self._skill = skill

    def get_level(self):
        return self._level

    def get_skill(self):
        return self._skill
