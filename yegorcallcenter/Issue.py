import abc
import random


class Issue(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self._id = id
        # 0 -> not resolved, 1 -> resolved
        self._status = 0
        self._difficulty = None

    @abc.abstractmethod
    def set_resolved(self):
        pass

    @abc.abstractmethod
    def get_status(self):
        pass

    @abc.abstractmethod
    def get_difficulty(self):
        pass


class BasicIssue(Issue):
    def __init__(self) -> None:
        super().__init__()
        self._difficulty = random.choice([0, 1, 2])

    """Description of issue. Is issue resolved or not

    Args:
        id (_type_): _description_
    """

    def set_resolved(self):
        self._status = 1

    def get_status(self):
        return self._status

    def get_difficulty(self):
        return self._difficulty
