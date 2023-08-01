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


def calculate_btu(units, room_type, height, length, width):
    result = height * length * width

    if room_type in ['lounge', 'dining room', 'bathroom']:
        result *= 5

    if room_type in ['bedroom']:
        result *= 4

    if room_type in ['kitchen', 'hallway']:
        result *= 3

    if units == "metres":
        result *= 35.3

    return result


def main():
    units = get_measurement_units()
    room_type = get_room_type()

    height = get_valid_float_input(
        f"Enter the height of the room in {units}: ")
    length = get_valid_float_input(
        f"Enter the length of the room in {units}: ")
    width = get_valid_float_input(f"Enter the width of the room in {units}: ")

    result = calculate_btu(units, room_type, height, length, width)
    result_str = "{:.1f}".format(result)
    
    print(f"{result_str} BTUs (British Thermal Units)")


if __name__ == "__main__":
    main()
