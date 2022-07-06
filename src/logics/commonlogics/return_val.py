from abc import abstractmethod


class IWeb:

    @abstractmethod
    def find(self):
        NotImplementedError

    @abstractmethod
    def clear(self):
        NotImplementedError




