n = 100

for p in range(2, n):
    for i in range(2, p-1):
        if p % i == 0:
            print(p, "is not a prime #")
            break
    else:
        print(p, "is a prime #")

print('that\'s a wrap!')