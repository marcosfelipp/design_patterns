'''
Example: Implementation of File System
(***) -> Directory
[--]  -> File

Directory can have a children but Files don't.
Representation of example:
       (***)
    /    |    \
  [--]  [--]  (***)
              /   \
            [--] [--]
Note: This code not handling exceptions 
'''

from abc import ABCMeta, abstractmethod

class Client():
    '''
    Manipulate objects of composite though Component interface, implementation of example described previously
    '''
    def __init__(self):
        documents   = Diretory('documents')
        pictures    = Diretory('pictures')
        word_file   = File('word_file')
        pdf_file    = File('pdf_file')
        pic_travel  = File('pic_travel')
        pic_car     = File('pic_car')

        documents.add(pdf_file)
        documents.add(word_file)
        documents.add(pictures)

        pictures.add(pic_travel)
        pictures.add(pic_car)

        node    = documents.get_children('pictures')
        pic     = node.get_children('pic_car')
        print(pic.name)

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
    def get_children(self, name):
        pass

    @abstractmethod
    def open_file(self):
        pass

class File(Component):
    '''
    Class that represents a file
    '''
    def __init__(self, name):
        self.name = name

    def open_file(self):
        print('File Opened')

    def add(self, node):
        pass

    def remove(self, node):
        pass

    def get_children(self, name):
        pass


class Diretory(Component):
    '''
    Class that represent a directory
    '''
    def __init__(self, name):
        self.name = name
        self.list_nodes = []

    def open_file(self):
        pass

    def add(self, node):
        self.list_nodes.append(node)

    def remove(self, node):
        pass

    def get_children(self, name):
        for node in self.list_nodes:
            if node.name == name :
                return node

if __name__ == '__main__':
    Client()