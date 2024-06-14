from abc import ABC
from car import Car


class Carrigan(ABC):
    def __init__(self, arr):
        self.condition = arr

    def needs_service(self):
        for i in self.condition:
            if i >= 0.9:
                return True
        return False
