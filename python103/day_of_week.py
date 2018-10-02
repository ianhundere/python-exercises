day = int(input('Day (0-6)? '))
answer = range(0,7)

try:
while day not in answer:
    day = int(input("Please enter a number 0-6: "))

if day == 0:
    print("Monday")
elif day == 1:
    print("Tuesday")
elif day == 2:
    print("Wednesday")
elif day == 3:
    print("Thursday")
elif day == 4:
    print("Friday")
elif day == 5:
    print("Saturday")
elif day == 6:
    print("Sunday")

except:
    print ("That was incorrect, try again.")