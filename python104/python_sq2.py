star_col = 0
star_row = 0

howBig = int(input("how big is the square? "))

while star_col < howBig:
    star_col += 1
    while star_row < howBig:
        print("*", end="")
        star_row += 1
    star_row = 0 
    print()
