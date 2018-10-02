height = int(input("height? "))

# each row is odd, so if x is 1 then there will be 1 star, x is 2 then 3 stars, x is 3 then 5 stars
for x in range(1, height + 1):
# the white space is always one less than the height and it decreases from there
    whitespace = height - x
    print((whitespace*" ")+(x + (x-1))*"*")
        

