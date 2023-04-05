import abc
import uuid

from yegorcallcenter import Caller, CallStatus, Employee, Issue


class Call(metaclass=abc.ABCMeta):
    def __init__(self, caller: Caller, issue: Issue) -> None:
        self._id = uuid.uuid4()
        self._caller = caller
        self._issue = issue

    @abc.abstractmethod
    def issue(self):
        pass

    @abc.abstractmethod
    def escalate(self):
        pass

    @abc.abstractmethod
    def resolved(self, e: Employee) -> bool:
        pass


class BasicCall(Call):
    def __init__(self, caller: Caller, issue: Issue) -> None:
        super().__init__(caller, issue)
        self._call_status = CallStatus.BasicCallStatus()

    def issue(self):
        return self._issue

    def escalate(self):
        # raise escalation level
        self._call_status.escalate_call()

    def resolved(self, e: Employee) -> bool:
        if self._issue.difficulty() <= e.qualification().level():
            self._issue.resolve()
            return True
        else:
            self.escalate()
            return False
