star_col = 0
star_row = 0

width = int(input("width? "))
height = int(input("height? "))
while star_col < height:
    star_col += 1
    while star_row < width:
        star_row += 1
        if star_col == 1:
            print("*", end="")
        elif star_row == 1:
            print("*", end="")
        elif star_col == height:
            print("*", end="")
        elif star_row == width:
            print("*", end="")
        else:
            print(" ", end="")
    star_row = 0
    print()
