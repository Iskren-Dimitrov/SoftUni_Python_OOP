from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(40, 150)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization_class_attributes(self):
        self.assertEqual(40, self.vehicle.fuel)
        self.assertEqual(40, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_when_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_without_raise_exception(self):
        self.vehicle.drive(1)

        self.assertEqual(38.75, self.vehicle.fuel)

    def test_when_fuel_is_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_when_capacity_is_more_than_fuel(self):
        self.vehicle.capacity = 100
        self.vehicle.refuel(1)

        self.assertEqual(41, self.vehicle.fuel)

    def test_return__str__message(self):
        self.assertEqual(f"The vehicle has 150 " +
                         f"horse power with 40 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()
