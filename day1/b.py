import aocd

f = aocd.get_data(day=1, year=2024)

left = []
right = []
similarity = 0

for currentLine in f.splitlines():
    left.append(int(currentLine.split()[0]))
    right.append(int(currentLine.split()[1]))

for i in range(0, len(left)):
    similarity += left[i] * right.count(left[i])

print(f"Similarity is: {similarity}.")