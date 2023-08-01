height = float(input("Enter the height of the room in your chosen measurement (cubic ft or metres): "))
length = float(input("Enter the length of the room in your chosen measurement (cubic ft or metres): "))
width = float(input("Enter the width of the room in your chosen measurement (cubic ft or metres): "))

result = height * length * width
print(f"{result} BTUs (British Thermal Units)")