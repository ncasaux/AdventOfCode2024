import aocd

f = aocd.get_data(day=5, year=2024)

total = 0

rules = f.split("\n\n")[0].splitlines()
updates = [l.split(",") for l in f.split("\n\n")[1].splitlines()]

for currentUpdate in updates:
    valid = True
    for i in range(len(currentUpdate)):
        for j in range(i + 1, len(currentUpdate)):
            pair = currentUpdate[i] + '|' + currentUpdate[j]
            if not pair in rules:
                valid = False
                break
    if valid: total += int(currentUpdate[int((len(currentUpdate) - 1) / 2)])

print(f"Count is: {total}.")
