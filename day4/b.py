import aocd

f = aocd.get_data(day=4, year=2024)

count = 0
tab = []
thickness = 1

for i in range(thickness):
    tab.append("." * (thickness * 2 + len(f.splitlines()[0])))

for currentLine in f.splitlines():
    tab.append("." * thickness + currentLine + "." * thickness)

for i in range(thickness):
    tab.append("." * (thickness * 2 + len(f.splitlines()[0])))

for y in range(len(tab)):
    for x in range(len(tab[0])):
        if tab[y][x] == "A":
            if (
                    (tab[y - 1][x - 1] == "M" and tab[y + 1][x + 1] == "S" or
                     tab[y - 1][x - 1] == "S" and tab[y + 1][x + 1] == "M") and
                    (tab[y + 1][x - 1] == "M" and tab[y - 1][x + 1] == "S" or
                     tab[y + 1][x - 1] == "S" and tab[y - 1][x + 1] == "M")
            ): count += 1

print(f"Count is: {count}.")