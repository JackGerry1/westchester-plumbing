def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    try:
        units = input("Enter your desired measurement units (ft or metres): ").lower()
        if units not in ['ft', 'metres']:
            raise ValueError("Invalid units. Please enter 'ft' or 'metres'.")

        height = get_valid_float_input(f"Enter the height of the room in {units}: ")
        length = get_valid_float_input(f"Enter the length of the room in {units}: ")
        width = get_valid_float_input(f"Enter the width of the room in {units}: ")

        # Add any additional calculations or processing here

        break  # Exit the loop if input is valid

    except ValueError as e:
        print(f"Error: {e}. Please try again.")


result = height * length * width

if units == "metres":
    result *= 35.3
    print(f"{result} BTUs (British Thermal Units)")
else:
    print(f"{result} BTUs (British Thermal Units)")
