for i in range(99, 0, -1):
    if i > 1:
        print (i, "bottles of beer on the wall,", i, "bottles of beer.")
        if i > 2:
            suffix = str(i -1) + " bottles of beer on the wall."
        else:
            suffix = "1 bottle of beer on the wall."
    elif i == 1:
        print ("1 bottle of beer on the wall, 1 bottle of beer.")
        suffix = "no more bottle of beer on the wall!"
    print ("Take one down, pass it around,", suffix)
    print ("done")