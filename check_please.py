import math

def split_check(total, number_of_people):
    cost_per_person = total / number_of_people
    return cost_per_person

amount_due = split_check(104.32, 5)
print("Each person owes ${}".format(amount_due))