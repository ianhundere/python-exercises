# the user provides a word with a vowel
word = input("Enter a word with a vowel: ").lower()

vowels = ["a", "e", "i", "o", "u"]
s = ''

for c in word:
    if c in vowels:
        s = s + c*5
    else:
        s = s + c

print(s)


# for c in word:
#     if c in vowels:
#         c = c*5
#         print(c, end='')
#     else:
#         print(c, end='')
