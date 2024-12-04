import aocd

f = aocd.get_data(day=4, year=2024)

count = 0
tab = []
thickness = 3

for i in range(thickness):
    tab.append("." * (thickness * 2 + len(f.splitlines()[0])))

for currentLine in f.splitlines():
    tab.append("." * thickness + currentLine + "." * thickness)

for i in range(thickness):
    tab.append("." * (thickness * 2 + len(f.splitlines()[0])))

for y in range(len(tab)):
    for x in range(len(tab[0])):
        if tab[y][x] == "X":
            if tab[y][x + 1] == "M" and tab[y][x + 2] == "A" and tab[y][x + 3] == "S": count += 1
            if tab[y][x - 1] == "M" and tab[y][x - 2] == "A" and tab[y][x - 3] == "S": count += 1
            if tab[y + 1][x] == "M" and tab[y + 2][x] == "A" and tab[y + 3][x] == "S": count += 1
            if tab[y - 1][x] == "M" and tab[y - 2][x] == "A" and tab[y - 3][x] == "S": count += 1
            if tab[y + 1][x + 1] == "M" and tab[y + 2][x + 2] == "A" and tab[y + 3][x + 3] == "S": count += 1
            if tab[y + 1][x - 1] == "M" and tab[y + 2][x - 2] == "A" and tab[y + 3][x - 3] == "S": count += 1
            if tab[y - 1][x - 1] == "M" and tab[y - 2][x - 2] == "A" and tab[y - 3][x - 3] == "S": count += 1
            if tab[y - 1][x + 1] == "M" and tab[y - 2][x + 2] == "A" and tab[y - 3][x + 3] == "S": count += 1

print(f"Count is: {count}.")