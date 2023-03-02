from yegorcallcenter import Call as Call
from yegorcallcenter import Employee as Employee


class CallCenter:
    def __init__(self, n_operator=1, n_supervisor=1, n_director=1) -> None:
        """CallCenter
            TODO: There must be at least one employee of each type
        Args:
            n_operator (int, optional): _description_. Defaults to 0.
            n_supervisor (int, optional): _description_. Defaults to 0.
            n_director (int, optional): _description_. Defaults to 0.
        """
        self._activecalls = []
        self._incommingcalls = []

        # initiate employees
        # 0 -> operator , 1 -> supervisor, 2 -> director
        self._employee = {0: [], 1: [], 2: []}
        self._queue = []

        for i in range(n_operator):
            self._employee[0].append(Employee.Operator())
        for i in range(n_supervisor):
            self._employee[1].append(Employee.Supervisor())
        for i in range(n_director):
            self._employee[2].append(Employee.Director())

    def incoming_call(self, call: Call):
        if call.get_issue().get_status() == 0:
            self._queue.append(call)
            print("Call intake - call ID: ", call._id)
            self.work()
        else:
            # call resolved
            pass

    # def escalate_call(self, call:C):

    # setup call center functionality
    # send employees to work
    # check if there is a call waiting and assign
    # to available employees
    def work(self):
        while self._queue:
            call = self._queue.pop(0)
            call_escal_level = call.get_escal_level()
            issue_dif = call.get_issue().get_difficulty()
            print(
                "Work - issue difficulty ",
                issue_dif,
                " esc level: ",
                call_escal_level,
                " queue: ",
                self._queue,
                " call ID: ",
                call._id,
            )
            # find free employee of this level
            emp = self._free_employee(call_escal_level)
            if not emp:
                self._queue.append(call)
            else:
                emp.set_busy()
                resolved = call.assign_employee(emp)
                emp.set_free()
                if not resolved:
                    self._queue.append(call)
                    print("Call escalated")
                else:
                    print("Call resolved")

    def _free_employee(self, level):
        # return free employee for level or None
        for e in self._employee[level]:
            if not e.is_busy():
                return e
        return None
