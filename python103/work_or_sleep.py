day = int(input('Day (0-6)? '))
answer = range(0,7)

while day not in answer:
    day = int(input("Please enter a number 0-6: "))

if day > 5:
    print("Sleep in")
else:
    print("Work day")
