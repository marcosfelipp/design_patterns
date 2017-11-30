'''
Example: Implementation of File System
'''

from abc import ABCMeta, abstractmethod

class Client():
    '''
    Manipulate objects of composite though Componet interface
    '''

class Component():

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_children(self):
        pass


class File():
    def add(self):
        pass

    def remove(self):
        pass

    def get_children(self):
        pass


class Diretory(Component):
    def __init__(self):
        pass

    def add(self):
        pass
    def remove(self):
        pass
    def get_children(self):
        pass