# Given an list of numbers, and a single factor (also a number),
# create a new list consisting of each of the numbers in the first list multiplied by the factor. 
# Print the new list out to the screen.

mult = [3, 9, 12, 15, 18, 21]
factor = 2
newMult = []

for x in mult:
    # factor * mult[x]
    newMult.append(x*factor)
print (newMult)
