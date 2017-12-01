'''
Example: Implementation of File System
(***) -> Diretory
[--]  -> File

Directory can have a children but Files don't.
Representation of example:
       (***)
    /    |    \
  [--]  [--]  (***)
              /   \
            [--] [--]
'''

from abc import ABCMeta, abstractmethod

class Client():
    '''
    Manipulate objects of composite though Component interface, implementation of example described previously
    '''
    def __init__(self):
        pass


class Component():
    '''
    Interface with methods to implement
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, node):
        pass
    @abstractmethod
    def remove(self, node):
        pass

    @abstractmethod
    def get_children(self):
        pass
    @abstractmethod
    def open_file(self):
        pass

class File(Component):
    def open_file(self):
        print('File Opened')


class Diretory(Component):
    def __init__(self):
        self.list_nodes = []

    def add(self, node):
        self.list_nodes.append(node)

    def remove(self, node):
        pass
    def get_children(self):
        return self.list_nodes.pop()

if __name__ == '__main__':
    Client()