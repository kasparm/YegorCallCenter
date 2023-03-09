import uuid

from yegorcallcenter import Caller, CallStatus, Employee, Issue


class Call:
    def __init__(self, caller: Caller, issue: Issue) -> None:
        self._id = uuid.uuid4()
        self._caller = caller
        self._issue = issue
        self._call_status = CallStatus.CallStatus()

    def get_issue(self):
        return self._issue

    def escalate(self):
        # raise escalation level
        self._call_status.escalate_call()

    def assign_employee(self, e: Employee) -> bool:
        if self._issue.get_difficulty() <= e.get_qualification().get_level():
            self._issue.set_resolved()
            return True
        else:
            self.escalate()
            return False
