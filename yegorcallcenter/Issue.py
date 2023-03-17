import abc
import random


class Issue(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self._id = id
        # 0 -> not resolved, 1 -> resolved
        self._status = 0
        self._difficulty = None

    @abc.abstractmethod
    def resolve(self):
        pass

    @abc.abstractmethod
    def status(self):
        pass

    @abc.abstractmethod
    def difficulty(self):
        pass


class BasicIssue(Issue):
    def __init__(self) -> None:
        super().__init__()
        self._difficulty = random.choice([0, 1, 2])

    """Description of issue. Is issue resolved or not

    Args:
        id (_type_): _description_
    """

    def resolve(self):
        self._status = 1

    def status(self):
        return self._status

    def difficulty(self):
        return self._difficulty
