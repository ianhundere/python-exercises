# var = 15
# print(f"This is my number: {var}")

# Out:

# This is my number: 15

# 1 X 1 = 1
# 1 X 2 = 2
# 1 X 3 = 3
# 1 X 4 = 4

# specify my iterator to multiply 

for l in range(1, 11):
    for r in range(1, 11):
        answer = (l*r)
        print(f"{l} X {r} = {answer}")
    
