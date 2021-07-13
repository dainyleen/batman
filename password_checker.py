import sys

password = input("Please enter a password: ")
attempt_count = 1
while password != 'cinderella':
    if attempt_count > 3:
        sys.exit("Too many invalid passowrd attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome, Cinderella!")