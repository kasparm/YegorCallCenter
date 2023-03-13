import abc
import uuid


class Caller(metaclass=abc.ABCMeta):

    """Caller class"""

    def __init__(self) -> None:
        self._id = uuid.uuid4()


class BasicCaller(Caller):
    def __init__(self, name=None) -> None:
        super().__init__()
        self._name = name if name else self._id
