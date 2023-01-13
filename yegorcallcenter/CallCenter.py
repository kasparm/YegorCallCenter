from yegorcallcenter import Employee as E
from yegorcallcenter import Call as C



class CallCenter():

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

        #initiate employees
        # 0 -> operator , 1 -> supervisor, 2 -> director
        self._employee = {0:[],1:[],2:[]}
        self._queue = []

        for i in range(n_operator):
            self._employee[0].append(E.Operator())
        for i in range(n_supervisor):
            self._employee[1].append(E.Supervisor())
        for i in range(n_director):
            self._employee[2].append(E.Director())

        self.work()



    def incomming_call(self, call:C):
        if call.get_issue().get_status() == 0:
            print(call.get_issue().get_status()," ",self._queue," ",call._id)
            self._queue.append(call)
            self.work()
        print(call.get_issue().get_status()," ",self._queue," ",call._id)

        
    #def escalate_call(self, call:C):

    # setup call center fuctionality
    # send employees to work
    # check if there is a call waiting and assing
    # to available employees
    def work(self):
        while self._queue:
            call = self._queue.pop(0)
            call_escal_level = call.get_escal_level()
            print("call_level: ",call_escal_level)
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
            
    def _free_employee(self, level):
        # return free employee for level or None
        for e in self._employee[level]:
                if not e.is_busy():
                    return e
        return None            
