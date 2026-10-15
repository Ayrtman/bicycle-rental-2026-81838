from rental_item import rental_item

class bicycle(rental_item):
    def __init__(self, item_id, brand, bike_type, rental_rate, gear_count):
        super().__init__(item_id, brand, rental_rate)
        self.bike_type = bike_type
        self.gear_count = int(gear_count)

    def rent_item(self):
        if self.is_rented:
            return False
        self.is_rented = True
        return True

    def return_item(self):
        if not self.is_rented:
            return False
        self.is_rented = False
        return True

    def calculate_rental_cost(self, duration_hours):
        cost = duration_hours * self.rental_rate
        if self.bike_type.lower() == "electric":
            cost = cost * 1.15
        return round(cost, 2)

    def to_file_line(self):
        return f"{self.item_id}|{self.brand}|{self.bike_type}|{self.rental_rate}|{self.gear_count}"

    @classmethod
    def from_file_line(cls, line):
        parts = line.strip().split("|")

        if len(parts) != 5:
            return None

        item_id = parts[0].strip()
        brand = parts[1].strip()
        bike_type = parts[2].strip()
        rate_str = parts[3].strip()
        gears_str = parts[4].strip()

        if not item_id or not brand or not bike_type or not rate_str or not gears_str:
            return None

        return cls(item_id, brand, bike_type, float(rate_str), int(gears_str))

    @classmethod
    def create_city_bike(cls, item_id, brand):
        return cls(item_id, brand, "Hybrid", 5.0, 7)

    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f"{self.item_id}: {self.brand} ({self.bike_type}) - €{self.rental_rate}/h [{status}]"