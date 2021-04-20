
### Dictionary

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit"


def validate_and_execute():

    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered number 0")
        else:
            print("You entered negative number")
    except ValueError:
        print("Invalid number entered")


user_input = ""
while user_input != "exit":
    user_input = input( "Enter number from days and conversion unit (2:hours):\n ")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0] ,"unit": days_and_unit[1]}
    print(days_and_unit)
    print(days_and_unit_dictionary)
    validate_and_execute()
