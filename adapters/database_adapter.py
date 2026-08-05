from abc import ABC, abstractmethod


class DatabaseAdapter(ABC):

    @abstractmethod
    def insert(self, records):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def query(self):
        pass

    @abstractmethod
    def update(self):
        pass