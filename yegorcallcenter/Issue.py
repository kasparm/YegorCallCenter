import random


class Issue:
    def __init__(self) -> None:
        """Description of issue. Is issue resolved or not

        Args:
            id (_type_): _description_
        """
        self._id = id
        # 0 -> not resolved, 1 -> resolved
        self._status = 0
        self._difficulty = random.choice([0, 1, 2])

    def set_resolved(self):
        self._status = 1

    def get_status(self):
        return self._status

    def get_difficulty(self):
        return self._difficulty
