from abc import ABC, abstractmethod

class Padder(ABC):
    @abstractmethod
    def pad(self, *args, **kwargs):
        pass

    @abstractmethod
    def unpad(self, *args, **kwargs):
        pass
