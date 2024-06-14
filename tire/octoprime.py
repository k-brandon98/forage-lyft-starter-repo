from abc import ABC
from car import Car


class Octoprime(ABC):
    def __init__(self, arr):
        self.condition = arr

    def needs_service(self):
        sum = 0
        for i in self.condition:
            sum += i

        if sum >= 3:
            return True
        else:
            return False
