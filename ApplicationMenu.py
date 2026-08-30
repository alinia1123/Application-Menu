from datetime import datetime

print("alinia1123 Spreadsheet Automation Menu")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores it into the variable called choice.
choice = input("Enter option: ")

print("You selected option", choice)
print("The time and date is", str(datetime.now()))
