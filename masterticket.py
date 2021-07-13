# Declare variables
TICKET_PRICE = 10
tickets_remaining = 100

# Output how many tickets are remaining using tickets_remaining variable
print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they would like
num_tickets = input("How many tickets would you like, {}? ".format(name) )

# Calculate the price (number of tickers multiplied by the price) and assign it to a variable
total_price = int(float(num_tickets * TICKET_PRICE))

# Output the price to the screen
print(total_price)

