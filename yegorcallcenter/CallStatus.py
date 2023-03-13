import abc


class CallStatus(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def in_progress(self):
        pass

    @abc.abstractmethod
    def get_escalation_level(self):
        pass

    @abc.abstractmethod
    def escalate_call(self):
        pass

    @abc.abstractmethod
    def set_in_progress(self):
        pass

    @abc.abstractmethod
    def set_not_in_progress(self):
        pass


class BasicCallStatus(CallStatus):
    def __init__(self) -> None:
        super().__init__()
        self._in_progress = True
        self._escalation_level = 0

    def in_progress(self):
        return self._in_progress

    def get_escalation_level(self):
        return self._escalation_level

    def escalate_call(self):
        self._escalation_level += 1

    def set_in_progress(self):
        self._in_progress = True

    def set_not_in_progress(self):
        self._in_progress = False
