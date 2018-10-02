star_col = 0
star_row = 0

while star_col < 5:
    print("*", end="")
    star_col += 1
    while star_row < 4:
        print("*", end="")
        star_row += 1
    star_row = 0
    print()
