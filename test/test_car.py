import unittest
from datetime import datetime

from battery.battery import Battery
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine
from battery import nubbin_battery
from battery import spindler_battery

class TestBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        today= datetime.today().date()
        last_service_date= today.replace(year=today.year -2)

        #battery = spindler_battery(last_service_date, current_mileage, last_service_mileage)
        #self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_be_serviced(self):
        today= datetime.today().date()
        last_service_date= today.replace(year=today.year -4)

        #battery = nubbin_battery(last_service_date, current_mileage, last_service_mileage)
        #self.assertTrue(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 3000
        last_service_mileage = 0

        engine= capulet_engine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        engine = sternman_engine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine= willoughby_engine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()