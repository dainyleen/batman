first_name = input("What is your first name? ")
print("Hello,", first_name)
if first_name == "Dainy":
    print(first_name, "is learning Python")
elif first_name == "Faye":
    print(first_name, "is learning with fellow students")
else:
    print("You should totally learn Python, {}".format(first_name))
print("Have a great day {}!".format(first_name))
