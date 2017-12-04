from threading import Thread
from abc import ABCMeta
from abc import abstractmethod
import time

class Subject():
    '''
    Class that send messages to assigned's classes 
    '''
    def __init__(self):
        self.observers = []

    def add_observers(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observers(self, observer):
        for obs in self.observers:
            if observer is obs:
                del(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            if isinstance(observer, ObserverInterface):
                observer.event_observable(event)

class ObserverInterface():
    '''
    Methods that want subscribe event implements this interface
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def event_observable(self, event):
        return NotImplemented

class Observer(Thread, ObserverInterface):
    def __init__(self, subject):
        Thread.__init__(self)
        self.subject = subject

    def run(self):
        for i in range(10):
            time.sleep(5)
            self.event_observable('call')

    def event_observable(self, event):
        self.subject.notify_observers(event)

class ObjObserver1(ObserverInterface):
    def event_observable(self, event):
        print(event)
        print('event received in observer 1')

class ObjObserver2(ObserverInterface):
    def event_observable(self, event):
        print(event)
        print('event received in observer 2')

if __name__ == "__main__":
    sub = Subject()

    # Classes that want observer event:
    obs_srv1 = ObjObserver1()
    obs_srv2 = ObjObserver2()

    # Add classes in observers
    sub.add_observers(obs_srv1)
    sub.add_observers(obs_srv2)

    obs = Observer(sub)
    obs.start()
