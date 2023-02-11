import uuid


class Caller:

    """Caller class"""

    def __init__(self, name=None) -> None:
        self._id = uuid.uuid4()
        self._name = name if name else self._id
