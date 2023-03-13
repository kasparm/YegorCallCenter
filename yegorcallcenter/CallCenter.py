import abc

from yegorcallcenter import Call, Employee


class CallCenter(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def incoming_call(self, call: Call):
        pass


class BasicCallCenter(CallCenter):
    def __init__(self, n_operator=1, n_supervisor=1, n_director=1) -> None:
        """CallCenter
            TODO: There must be at least one employee of each type
        Args:
            n_operator (int, optional): _description_. Defaults to 0.
            n_supervisor (int, optional): _description_. Defaults to 0.
            n_director (int, optional): _description_. Defaults to 0.
        """
        super().__init__()
        self._active_calls = []
        self._incoming_calls = []

        # initiate employees
        # 0 -> operator , 1 -> supervisor, 2 -> director
        self._employee = {0: [], 1: [], 2: []}
        self._call_queue = []

        for i in range(n_operator):
            self._employee[0].append(Employee.Operator())
        for i in range(n_supervisor):
            self._employee[1].append(Employee.Supervisor())
        for i in range(n_director):
            self._employee[2].append(Employee.Director())

    def incoming_call(self, call: Call):
        if call.get_issue().get_status() == 0:
            self._call_queue.append(call)
            print("Call intake - call ID: ", call._id)
            self._work()
        else:
            # call resolved
            pass

    # def escalate_call(self, call:C):

    # setup call center functionality
    # send employees to work
    # check if there is a call waiting and assign
    # to available employees
    def _work(self):
        while self._call_queue:
            call = self._call_queue.pop(0)
            call_escalate_level = call._call_status.get_escalation_level()
            issue_difficulty = call.get_issue().get_difficulty()
            print(
                "Work - issue difficulty ",
                issue_difficulty,
                " esc level: ",
                call_escalate_level,
                " queue: ",
                self._call_queue,
                " call ID: ",
                call._id,
            )
            # find free employee of this level
            emp = self._free_employee(call_escalate_level)
            if not emp:
                self._call_queue.append(call)
            else:
                emp.set_busy()
                resolved = call.resolved(emp)
                emp.set_free()
                if not resolved:
                    self._call_queue.append(call)
                    print("Call escalated")
                else:
                    print("Call resolved")

    def _free_employee(self, level):
        # return free employee for level or None
        for e in self._employee[level]:
            if not e.is_busy():
                return e
        return None
