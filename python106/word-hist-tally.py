histo = input("Enter a sentence: ").split()
wordDict = {}

for word in histo:
    if word in wordDict:
       wordDict[word] += 1
    else:
       wordDict[word] = 1


# newDict = max(dict, key=dict.get)[:3] < --- this only gave me the max value when i was looking for the 3 max values.
# newDict = sorted(wordDict.items(), reverse=True)[:3]
newDict = sorted(wordDict.items(), key = lambda a: a[1], reverse=True)[:3]


print("The top three words are:")
for newvalue, newvalue2 in newDict:
    print(newvalue,":", newvalue2)

