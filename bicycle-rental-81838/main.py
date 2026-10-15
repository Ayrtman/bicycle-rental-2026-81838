from bicycle import bicycle

fleet = [
    bicycle("B001", "Trek", "Mountain", 8.0, 21),
    bicycle("B002", "Specialized", "Electric", 12.0, 10),
    bicycle.from_file_line("B003|Giant|Road|10.0|18"),
    bicycle.create_city_bike("B004", "Raleigh")
]

def find_bike_by_id(bike_id):
    for bike in fleet:
        if bike.item_id.lower() == bike_id.lower():
            return bike
    return None

while True:
    print("\nBicycle Rental System")
    print("1. Show all bicycles")
    print("2. Search bicycle by ID")
    print("3. Rent a bicycle")
    print("4. Return a bicycle")
    print("5. Add bicycle")
    print("6. Exit")

    choice = input("choose an option: ").strip()

    if choice == "1":
        for current_bike in fleet:
            print(current_bike)

    elif choice == "2":
        bike_id = input("bicycle ID: ").strip()
        found_bike = find_bike_by_id(bike_id)

        if found_bike is None:
            print("Bicycle not found.")
        else:
            print(found_bike)

    elif choice == "3":
        bike_id = input("bicycle ID: ").strip()
        found_bike = find_bike_by_id(bike_id)

        if found_bike is None:
            print("Bicycle not found.")
            continue

        if found_bike.is_rented:
            print("Bicycle is already rented.")
        else:
            found_bike.rent_item()
            print("Bicycle rented successfully.")

    elif choice == "4":
        bike_id = input("bicycle ID: ").strip()
        found_bike = find_bike_by_id(bike_id)

        if found_bike is None:
            print("Bicycle not found.")
            continue

        if not found_bike.is_rented:
            print("Bicycle was not rented.")
            continue

        hours = float(input("rental duration in hours: ").strip())
        cost = found_bike.calculate_rental_cost(hours)
        found_bike.return_item()
        print(f"Bicycle returned. Total cost: €{cost:.2f}")

    elif choice == "5":
        bike_id = input("bicycle ID: ").strip()
        brand = input("bicycle brand: ").strip()
        bike_type = input("bicycle type: ").strip()
        rental_rate = input("rental rate: ").strip()
        gear_count = input("gear count: ").strip()

        if not bike_id or not brand or not bike_type or not rental_rate or not gear_count:
            print("Input error: all fields are required")
            continue

        existing_bike = find_bike_by_id(bike_id)
        if existing_bike is not None:
            print("A bicycle with ID already exists.")
            continue

        new_bike = bicycle(bike_id, brand, bike_type, float(rental_rate), int(gear_count))
        fleet.append(new_bike)
        print("Bicycle saved.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1 to 6.")