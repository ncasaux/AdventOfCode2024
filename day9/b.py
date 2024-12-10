import aocd

f = aocd.get_data(day=9, year=2024)
content = []
blanks = []
quantity = {}
checksum = 0

for i in range(len(f)):
    if i % 2 == 0:
        content.extend([int(i // 2)] * int(f[i]))
        quantity[int(i // 2)] = int(f[i])
    else:
        content.extend("." * int(f[i]))

for i in range(len(content)):
    if content[i] == ".": blanks.append(i)

for i in range(len(content) - 1, 0, -1):
    if content[i] == ".":
        continue
    if blanks[0] < i:
        for k in range(len(blanks) - quantity[content[i]]):
            if blanks[quantity[content[i]] - 1 + k] - blanks[k] + 1 == quantity[content[i]] and blanks[k] < i:
                for j in range(quantity[content[i]]):
                    content[blanks[k]] = content[i - j]
                    blanks.pop(k)
                    content[i - j] = "."
                break

for i in range(len(content)):
    if content[i] == ".": continue
    checksum += int(content[i]) * i

print(f"Checksum: {checksum}")
