import aocd
import re

f = aocd.get_data(day=3, year=2024)

def calculate_sum(l):
    r = re.findall("mul\\((\\d+),(\\d+)\\)", l)
    return sum([int(t[0]) * int(t[1]) for t in r])

result = 0
concatenatedLines = ""

for currentLine in f.splitlines():  concatenatedLines += currentLine

DONT_substring = concatenatedLines.split("don't()")
result += calculate_sum(DONT_substring[0])

for i in DONT_substring[1:]:
    DO_substring = str(i).split("do()")
    if len(DO_substring) > 1:
        for j in DO_substring[1:]:
            result += calculate_sum(j)

print(f"Result is: {result}.")


