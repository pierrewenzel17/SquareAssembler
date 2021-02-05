from abc import abstractmethod


class Observer:
    @abstractmethod
    def update(self, data) -> None:
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