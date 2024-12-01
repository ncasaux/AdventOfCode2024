import aocd

f = aocd.get_data(day=1, year=2024)

left = []
right = []
distance = 0

for currentLine in f.splitlines():
    left.append(int(currentLine.split()[0]))
    right.append(int(currentLine.split()[1]))

left.sort()
right.sort()

for i in range(0, len(left)):
    distance += abs(left[i] - right[i])

print(f"Distance is: {distance}.")