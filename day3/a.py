import aocd
import re

f = aocd.get_data(day=3, year=2024)

result = 0

for currentLine in f.splitlines():
    r = re.findall("mul\\((\\d+),(\\d+)\\)", currentLine)
    result += sum([int(t[0]) * int(t[1]) for t in r])

print(f"Result is: {result}.")