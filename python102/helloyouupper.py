name = input('what is your name? '.upper())
answer = "hello " + name + " ! "
letters = "your name has %d letters in it! awesome!" % len(name)

print(answer.upper() + letters.upper())