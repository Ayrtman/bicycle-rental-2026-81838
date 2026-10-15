from abc import ABC, abstractmethod

class rental_item(ABC):
    def __init__(self, item_id, brand, rental_rate):
        self.item_id = item_id
        self.brand = brand
        self.rental_rate = float(rental_rate)
        self.is_rented = False

    @abstractmethod
    def rent_item(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def calculate_rental_cost(self, duration_hours):
        pass