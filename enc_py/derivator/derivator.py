from abc import ABC, abstractmethod

class Derivator(ABC):
    @abstractmethod
    def derive(self, *args, **kwargs):
        pass
