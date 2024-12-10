import aocd

f = aocd.get_data(day=9, year=2024)

content = []
checksum = 0

for i in range(len(f)):
    if i % 2 == 0:
        content.extend([int(i // 2)] * int(f[i]))
    else:
        content.extend("." * int(f[i]))

for i in range(len(content) - 1, 0, -1):
    if content[i] == ".":
        continue
    if content.index(".") < i:
        content[content.index(".")] = content[i]
        content[i] = "."

for i in range(len(content)):
    if content[i] == ".": continue
    checksum += int(content[i]) * i

print(f"Checksum: {checksum}")
