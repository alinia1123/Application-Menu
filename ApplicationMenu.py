from datetime import datetime

menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}

print("alinia1123 Spreadsheet Automation Menu")

for number, option in menu_options.items():
    print(number + ".", option)

choice = input("Enter option: ")

if choice in menu_options:
    print("You selected option", choice)
    print("The time and date is", str(datetime.now()))
else:
    print("Error: Invalid choice selected")
