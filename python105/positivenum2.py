numList = [-5, -4, -3, -2, -1 , 0, 1, 2, 3, 4, 5]
numList2 = []

for x in numList:
  if x == 6:
    break
  elif x > 0:
    numList2.append(x)

print(numList2)
