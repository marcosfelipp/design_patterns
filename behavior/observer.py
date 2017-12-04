from threading import Thread
import time

class Subject():
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
            if isinstance(observer, Observer):
                observer.event_observable(event)

class Observer(Thread):
    def __init__(self, subject):
        Thread.__init__(self)
        self.subject = subject

    def run(self):
        time.sleep(5)
        self.event_observable('call')

    def event_observable(self, event):
        self.subject.notify_observers(event)

class ObjObserver(Observer):
    pass

if __name__ == "__main__":
    pass