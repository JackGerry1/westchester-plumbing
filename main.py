def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_measurement_units():
    while True:
        units = input(
            "Enter your desired measurement units (ft or metres): ").lower()
        if units not in ['ft', 'metres']:
            print("Invalid units. Please enter 'ft' or 'metres'.")
        else:
            return units


def get_room_type():
    while True:
        room_type = input(
            "Enter the room type you are measuring (Lounge, Dining Room, Bedroom, Hallway, Kitchen, and Bathroom): ").lower()
        if room_type not in ['lounge', 'dining room', 'bedroom', 'hallway', 'kitchen', 'bathroom']:
            print("Invalid room type. Please enter a valid room type.")
        else:
            return room_type


def get_facing_direction():
    return get_bool_input("Is the room facing North? (yes/no): ")


def get_french_windows():
    return get_bool_input("Does the room have French windows? (yes/no): ")


def get_double_glazing():
    return get_bool_input("Does the room have double glazing? (yes/no): ")


def get_bool_input(prompt):
    while True:
        value = input(prompt).lower()
        if value in ['yes', 'no']:
            return value
        print("Invalid input. Please enter 'yes' or 'no'.")


def calculate_btu(units, room_type, height, length, width, facing, french_windows, double_glazing):
    result = height * length * width

    if room_type in ['lounge', 'dining room', 'bathroom']:
        result *= 5

    elif room_type in ['bedroom']:
        result *= 4

    elif room_type in ['kitchen', 'hallway']:
        result *= 3

    if units == "metres":
        result *= 35.3

    if facing == "yes":
        result *= 1.15

    if french_windows == "yes":
        result *= 1.20

    if double_glazing == "yes":
        result *= 0.90

    return result


def main():
    units = get_measurement_units()
    room_type = get_room_type()

    height = get_valid_float_input(
        f"Enter the height of the room in {units}: ")

    length = get_valid_float_input(
        f"Enter the length of the room in {units}: ")

    width = get_valid_float_input(f"Enter the width of the room in {units}: ")

    facing = get_facing_direction()
    french_windows = get_french_windows()
    double_glazing = get_double_glazing()

    result = calculate_btu(units, room_type, height, length, width, facing, french_windows, double_glazing)
    
    result_str = "{:.1f}".format(result)

    print(f"{result_str} BTUs (British Thermal Units)")


if __name__ == "__main__":
    main()
