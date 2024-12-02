import aocd

f = aocd.get_data(day=2, year=2024)

line = []
diffLine = []
safe = 0

for currentLine in f.splitlines():
    line = list(map(int, currentLine.split()))

    for i in range(0, len(line)):
        modifiedLine = line.copy()
        modifiedLine.pop(i)
        diffLine = [modifiedLine[i + 1] - modifiedLine[i] for i in range(0, len(modifiedLine) - 1)]
        if min(diffLine)>=1 and max(diffLine)<=3 or min(diffLine)>=-3 and max(diffLine)<=-1:
            safe+=1
            break

print(f"Number of safe reports: {safe}.")