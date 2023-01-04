from yegorcallcenter import Caller,Issue
import uuid
class Call():
    def __init__(self, caller: Caller, issue: Issue) -> None:
        self._id = uuid.uuid4()
        self._caller = caller
        self._issue = issue
        self._in_progress = True
        self._employee = []
        

    def get_issue(self):
        return self._issue