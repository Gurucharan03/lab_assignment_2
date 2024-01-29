# Employee Table data
employee_data = [
    {"Employee ID": "161E90", "Name": "Ramu", "Age": 35, "Salary": 59000},
    {"Employee ID": "171E22", "Name": "Tejas", "Age": 30, "Salary": 82100},
    {"Employee ID": "171G55", "Name": "Abhi", "Age": 25, "Salary": 100000},
    {"Employee ID": "152K46", "Name": "Jaya", "Age": 32, "Salary": 85000},
]

def print_table(data):
    # Print table header
    header = ["Employee ID", "Name", "Age", "Salary"]
    print(f"{header[0]:<10} {header[1]:<10} {header[2]:<5} {header[3]:<10}")

    # Print table rows
    for row in data:
        print(f"{row['Employee ID']:<10} {row['Name']:<10} {row['Age']:<5} {row['Salary']:<10}")

def sort_table(data, key, reverse=False):
    # Sort the table based on the specified key
    sorted_data = sorted(data, key=lambda x: x[key], reverse=reverse)
    return sorted_data

# Main program
while True:
    print("\nEmployee Table:")
    print_table(employee_data)

    print("\nOptions:")
    print("1. Sort by Employee ID")
    print("2. Sort by Name")
    print("3. Sort by Age")
    print("4. Sort by Salary")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting program.")
        break
    elif choice in ['1', '2', '3', '4']:
        reverse_order = input("Sort in descending order? (y/n): ").lower() == 'y'
        key = ["Employee ID", "Name", "Age", "Salary"][int(choice) - 1]
        sorted_data = sort_table(employee_data, key, reverse_order)
        print(f"\nSorted by {key} in {'descending' if reverse_order else 'ascending'} order:")
        print_table(sorted_data)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
