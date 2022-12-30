from abc import ABCMeta, abstractclassmethod
import uuid
class Employee(metaclass=ABCMeta):
    def __init__(self, name, level) -> None:
        """Employee of the call center

        Args:
            id (int): ID of the employee
            name (string): name of the employee, default is id
            level (int): level of the employee 0 = operator, 1 = supervisor, 2 =director 
        """
        self._id = uuid.uuid4()
        self.name = name
        self.level = level



class Operator(Employee):

    def __init__(self, name=uuid.uuid4(), level=0) -> None:
        super().__init__(name, level)
        print(name)

class Supervisor(Employee):

    def __init__(self, name=uuid.uuid4(), level=1) -> None:
        super().__init__(name, level)
        
class Director(Employee):

    def __init__(self, name=uuid.uuid4(), level=2) -> None:
        super().__init__(name, level)