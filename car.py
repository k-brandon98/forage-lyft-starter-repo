from abc import ABC
from battery import battery
from engine import engine

class Car(ABC):
    def __init__(self, engine: engine.Engine, battery: battery.Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        eng_service = self.engine.engine_should_be_serviced()
        bat_service = self.battery.needs_service()
        return eng_service or bat_service
