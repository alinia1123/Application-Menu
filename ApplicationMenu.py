from datetime import datetime

menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}

# This function takes a number in pounds and returns the converted weight in kilograms.
def convertData(data):
    converted = data / 2.205
    return converted


def getInput():
    entries = int(input("How many entries are you inputting? "))

    for number in range(entries):
        date = input("Enter a date: ")
        weight = int(input("Enter the weight in pounds for the inputted date: "))

        # Calls convertData using the weight as the argument and returns the converted weight.
        convertedWeight = convertData(weight)

        print("The following was saved at", datetime.now(), ",", date, weight, convertedWeight)


print("alinia1123 Spreadsheet Automation Menu")
print("Choose a menu item from the following options")

for number, option in menu_options.items():
    print(number + ".", option)

choice = input("Enter option: ")

if choice == "1":
    print("You selected", choice, "at", datetime.now())
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
