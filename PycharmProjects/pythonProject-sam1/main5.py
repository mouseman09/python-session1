

my_list = ["January", "February","March"]
print(my_list[0])
my_list.append("April")
print(f"Length of my list is  {my_list.__len__()}")
print("Length of my list is " + str(my_list.__len__()))

to_units = 24
name_of_unit = "hours"
my_set = {"Jan","Feb","Mar"}


### Sets

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

user_input = ""
while user_input != "exit":
    user_input = input( "Enter a valid number:\n ")
    print(set(user_input))
    print(type(set(user_input)))
   for num_of_days_element in set(user_input.split(", ")):
       validate_and_execute()
