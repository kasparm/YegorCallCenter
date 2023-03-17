import abc


class CallStatus(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def in_progress(self):
        pass

    @abc.abstractmethod
    def escalation_level(self):
        pass

    @abc.abstractmethod
    def escalate_call(self):
        pass

    @abc.abstractmethod
    def start_call(self):
        pass

    @abc.abstractmethod
    def stop_call(self):
        pass


class BasicCallStatus(CallStatus):
    def __init__(self) -> None:
        super().__init__()
        self._in_progress = True
        self._escalation_level = 0

    def in_progress(self):
        return self._in_progress

    def escalation_level(self):
        return self._escalation_level

    def escalate_call(self):
        self._escalation_level += 1

    def start_call(self):
        self._in_progress = True

    def stop_call(self):
        self._in_progress = False
