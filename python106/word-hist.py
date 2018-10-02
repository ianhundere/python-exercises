histo = input("Enter a sentence: ").split()
wordDict = {}

for word in histo:
    if word in wordDict:
       wordDict[word] += 1
    else:
       wordDict[word] = 1

print(wordDict)
