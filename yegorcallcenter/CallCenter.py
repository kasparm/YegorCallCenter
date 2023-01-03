from yegorcallcenter import Employee as E
from yegorcallcenter import Call as C



class CallCenter():

    def __init__(self, n_operator=0, n_supervisor=0, n_director=0) -> None:
        """_summary_

        Args:
            n_operator (int, optional): _description_. Defaults to 0.
            n_supervisor (int, optional): _description_. Defaults to 0.
            n_director (int, optional): _description_. Defaults to 0.
        """
        self._activecalls = []
        #initiate employees
        self._employee = []
        self._queue = []

        for i in range(n_operator):
            self._employee.append(E.Operator())
        for i in range(n_supervisor):
            self._employee.append(E.Supervisor())
        for i in range(n_director):
            self._employee.append(E.Director())



    def incomming_call(self, call:C):
        self._activecalls.append(call)
        

