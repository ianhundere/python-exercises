secret = "lbh zhfg hayrnea jung lbh unir yrnearq"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

decoded_msg = ""

for letter in secret:
    if letter not in abc:
        decoded_msg = letter
    else:
        decoded_msg = abc[(abc.find(letter)+13) % 26]
    print(decoded_msg, end='')





# neat stuff
# import string
# print(string.ascii_lowercase)
