from abc import ABC, abstractmethod

class Hashing(ABC):

    @abstractmethod
    def get_hashes(self, item: str, array_size: int, no_of_hashes: int):
        pass


