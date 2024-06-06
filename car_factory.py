from abc import ABC
import battery
import battery.nubbin_battery
import battery.spindler_battery
import engine
from car import Car
from datetime import datetime

import engine.capulet_engine
import engine.sternman_engine
import engine.willoughby_engine

class CarFactory(ABC):
  def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
    self.current_date = datetime.today().date()
    self.last_service_date = last_service_date
    self.current_mileage = current_mileage
    self.last_service_mileage = last_service_mileage
    self.warning_light_is_on = warning_light_is_on

  def create_calliope(self):
    eng = engine.capulet_engine.CapuletEngine(self.current_mileage, self.last_service_mileage)
    bat = battery.spindler_battery.SpindlerBattery(self.last_service_date)
    return Car(eng, bat)
  
  def create_thovex(self):
    eng = engine.capulet_engine.CapuletEngine(self.current_mileage, self.last_service_mileage)
    bat = battery.nubbin_battery.NubbinBattery(self.last_service_date)
    return Car(eng, bat)
  
  def create_glissade(self):
    eng = engine.willoughby_engine.WilloughbyEngine(self.current_mileage, self.last_service_mileage)
    bat = battery.spindler_battery.SpindlerBattery(self.last_service_date)
    return Car(eng, bat)

  def create_rorschach(self):
    eng = engine.willoughby_engine.WilloughbyEngine(self.current_mileage, self.last_service_mileage)
    bat = battery.nubbin_battery.NubbinBattery(self.last_service_date)
    return Car(eng, bat)

  def create_palindrome(self):
    eng = engine.sternman_engine.SternmanEngine(self.warning_light_is_on)
    bat = battery.spindler_battery.SpindlerBattery(self.last_service_date)
    return Car(eng, bat)
  