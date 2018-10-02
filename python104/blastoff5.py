import time 
start = int(input("enter a number: "))
while start >= 20:
    start = int(input("please enter a number below 20: "))
start = start + 1
end = 0

while start > end:
    start -= 1
    time.sleep(1)
    print(start)
    if start == 0:
        print("we're done!")
    else:
        pass
