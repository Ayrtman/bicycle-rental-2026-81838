import unittest
from rental_item import rental_item
from bicycle import bicycle

class TestBicycle(unittest.TestCase):
    def setUp(self):
        self.bike = bicycle("B1", "Trek", "Mountain", 10.0, 21)

    def test_bike_data(self):
        self.assertEqual(self.bike.item_id, "B1")
        self.assertEqual(self.bike.brand, "Trek")

    def test_cannot_create_rental_item_directly(self):
        with self.assertRaises(TypeError):
            rental_item("X1", "Generic", 5.0)

    def test_rent_success(self):
        self.assertTrue(self.bike.rent_item())
        self.assertTrue(self.bike.is_rented)

    def test_rent_already_rented_fails(self):
        self.bike.rent_item()
        self.assertFalse(self.bike.rent_item())

    def test_return_success(self):
        self.bike.rent_item()
        self.assertTrue(self.bike.return_item())
        self.assertFalse(self.bike.is_rented)

    def test_return_not_rented_fails(self):
        self.assertFalse(self.bike.return_item())

    def test_cost_normal(self):
        self.assertEqual(self.bike.calculate_rental_cost(2.0), 20.0)

    def test_cost_electric(self):
        ebike = bicycle("B2", "Volt", "Electric", 10.0, 7)
        self.assertEqual(ebike.calculate_rental_cost(2.0), 23.0)

    def test_from_file_line(self):
        b = bicycle.from_file_line("B3|Giant|Road|15.0|18")
        self.assertIsNotNone(b)
        self.assertEqual(b.brand, "Giant")

    def test_create_city_bike(self):
        city = bicycle.create_city_bike("B4", "Raleigh")
        self.assertEqual(city.bike_type, "Hybrid")

if __name__ == "__main__":
    unittest.main()