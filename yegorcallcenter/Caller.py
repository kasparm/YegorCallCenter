import uuid

class Caller:
    
    """ Caller class"""
    def __init__(self, name) -> None:
        self._name = name
        self._id = uuid.uuid4()