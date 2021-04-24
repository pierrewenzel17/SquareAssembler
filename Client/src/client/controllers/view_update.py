from abc import abstractmethod


class Observer:
    @abstractmethod
    def update(self, data) -> None:
        pass

    @abstractmethod
    def update_obline(self, data,iserveur) -> None:
        pass
    @abstractmethod
    def update_quit(self):
        pass


class Observable:

    def __init__(self) -> None:
        self.list_observers: list[Observer] = []

    def notify(self, data) -> None:
        for observer in self.list_observers:
            observer.update(data)

    def add_observer(self, observer: Observer) -> None:
        self.list_observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.list_observers.remove(observer)

    def notify_online(self,data,iserveur):
        for observer in self.list_observers:
            observer.update_obline(data,iserveur)

    def notify_quit(self):
        for observer in self.list_observers:
            observer.update_quit()