print("Thank you Lord")
print(f"Test Add {200 + 300}")
print(f"Test Multiply {200 * 300}")

addMe = 30 + 60
print(f"Test Add thro variable: {addMe}")

addMe_Multiply = 2
print(f"Test the add and multiply: {addMe * addMe_Multiply}")

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good")


days_to_units()

def days_to_units_param(num_of_days):
    print(str("============="))
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print("All good")

days_to_units_param(10)

def scope_check():
    local_var = 1
    print(f"Global variable: {calculation_to_units}")
    print (f"Local Variable: {local_var}")


scope_check()

### new code
user_input = input("Enter a Number of Days:\n ")
print (type(user_input))
user_input = int(user_input)
print (type(user_input))
if (user_input > 0):
    days_to_units_param(int(user_input))
elif user_input == 0:
    print ("Enter a number greater than 0")
else:
    print ("Invalid number")

### new code




