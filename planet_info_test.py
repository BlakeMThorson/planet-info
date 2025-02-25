import unittest
from planet_info import Planet

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        self.first_planet = Planet("first", 10, 10, 10, [])
        self.second_planet = Planet("second", 100, 100, 100, ["da moon"])
        self.third_planet = Planet("third", 100, 100, 100, ["da moon", "the moon", "a moon"])

    def test_distance_from_another_planet(self):
        assert self.first_planet.distance_from_another_planet(self.second_planet) == 90
        assert self.second_planet.distance_from_another_planet(self.first_planet) == 90

    def test_compare_mass_to_another_planet(self):
        assert self.first_planet.compare_mass_to_another_planet(self.second_planet) == "first is 90kg lighter than second"
        assert self.second_planet.compare_mass_to_another_planet(self.second_planet) == "second is 0kg heavier than second"
        assert self.second_planet.compare_mass_to_another_planet(self.first_planet) == "second is 90kg heavier than first"

    def test_format_moons(self):
        assert self.first_planet.format_moons() == "first has no moons."
        assert self.second_planet.format_moons() == "second has the following moon: da moon."
        assert self.third_planet.format_moons() == "third has the following moons: da moon, the moon, a moon."

    def test_basic_info(self):
        assert self.first_planet.name == "first"
        assert self.first_planet.mass == 10
        assert self.first_planet.distance_from_sun == 10
        assert self.first_planet.moon_count == 10
        assert self.first_planet.moons == []

if __name__ == "__main__":
    unittest.main()