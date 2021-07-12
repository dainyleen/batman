first_name = input("What is your first name? ")
print("Hello,", first_name)
if first_name == "Dainy":
    print(first_name, "is learning Python")
elif first_name == "Faye":
    print(first_name, "is learning with fellow students")
else:
    # This is just in case we have a younger user 
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading already...".format(age))

    print("You should totally learn Python, {}".format(first_name))
print("Have a great day {}!".format(first_name))
