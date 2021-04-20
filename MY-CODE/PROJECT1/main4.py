

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():

    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered number 0")
        else:
            print("You entered negative number")
    except ValueError:
        print("Invalid number entered")


user_input = ""
while user_input != "exit":
    user_input = input( "Enter a valid number:\n ")
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()

