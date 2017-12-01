'''
Obs: Decorator pattern is different of decorator of Python
Example: 
'''
from abc import abstractmethod
from abc import ABCMeta

class Componente():
    __metaclass__ = ABCMeta

    @abstractmethod
    def method(self):
        pass

class Decorator():
    pass

class ConcreteComponent():
    pass

class ConcreteDecorator():
    pass
