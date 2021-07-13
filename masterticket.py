# Declare variables
TICKET_PRICE = 10
tickets_remaining = 100

# Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    try:
       num_tickets = int(num_tickets)
    except ValueError:
        print("Oh no, we ran into an issue. Please try again")
    else:
        total_price = num_tickets * TICKET_PRICE
        print("The total due is ${}".format(total_price))

        # Prompt usser if they want to proceed
        should_proceed = input("Do you want to proceed? Y/N ")
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))

print("Sorry, tickets are sold out.")

