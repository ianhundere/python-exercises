total = float(input('Total bill amount? '))
good = total * .20
fair = total * .15
bad = total * .10

service = input('Level of service? ')

split = float(input('Split how many ways? '))

if service == "good":
    print("Tip amount: $%.2f" % (good))
    print("Total amount: $%.2f" % (total + good))
    print("Amount per person: $%.2f" % (total / split))
elif service == "fair":
    print("Tip amount: $%.2f" % (fair))
    print("Total amount: $%.2f" % (total + fair))
    print("Amount per person: $%.2f" % (total / split))
elif service == "bad":
    print("Tip amount: $%.2f" % (bad))
    print("Total amount: $%.2f" % (total + bad))
    print("Amount per person: $%.2f" % (total / split))
