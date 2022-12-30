import itertools

class Issue():
    id = itertools.count()
    def __init__(self) -> None:
        """Description of issue. Is issue resolved or not

        Args:
            id (_type_): _description_
        """
        self._id = id
        self._status = 0
    def set_resolved(self):
        self._status = 1