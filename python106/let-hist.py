histo = input("Enter a word: ")
letterDict = {}

for letter in histo:
    if letter in letterDict:
       letterDict[letter] += 1
    else:
       letterDict[letter] = 1
    # letterDict[letter] = letterDict.get (letter, 0) +1
print(letterDict)


