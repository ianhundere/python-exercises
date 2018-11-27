leetme = input("Enter something to leetify: ").upper()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

leet = ["4", "8", "<", "|)", "3", "|=", "6", "4", "1", "7", "|<", 
"|_", "44", "|\|", "0", "|o", "9", "|2", "5", "7", "|_|", 
"\/", "\/\/", "%", "`/", "2"]

pos = 0

for x in abc:
    leetme = leetme.replace(x, leet[pos])
    pos += 1
print(leetme)
# while count < len(leetme):
#     currentletter = leetme[count]
#     count+=1
#     while abc[str.find] == leet[0:25]
#         leet.append(leet)
        



# def replace(abc, leet):
#    for lst in abc:
#       for ind, item in enumerate(lst):
#           lst[ind] = leet.get(item, item)
#           return leetme
        
# replace(abc,leet)
