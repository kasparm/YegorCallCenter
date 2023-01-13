from yegorcallcenter import Caller,Issue, Employee
import uuid
class Call():
    def __init__(self, caller: Caller, issue: Issue) -> None:
        self._id = uuid.uuid4()
        self._caller = caller
        self._issue = issue
        self._in_progress = True
        self._escal_level = 0 # 0=intake;1=escalate lavel 1; 2=escalate level 2
        self._employee = []
        

    def get_issue(self):
        return self._issue
    def get_escal_level(self):
        return self._escal_level

    def assign_employee(self, e:Employee) -> bool:
        self._employee.append(e)
        if self._issue.get_difficulty() <= e.get_level():
            self._issue.set_resolved()
            return True
        else:
            self._escal_level += 1
            return False