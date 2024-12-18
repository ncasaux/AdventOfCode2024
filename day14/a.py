import aocd
import re

f = aocd.get_data(day=14, year=2024)
rows, cols = 103, 101
seconds = 100
positions = {}
q1 = q2 = q3 = q4 = 0

robots = f.splitlines()

for robot in robots:
    match = re.match("p=(?P<cn>-?\\d+),(?P<rn>-?\\d+) v=(?P<cs>-?\\d+),(?P<rs>-?\\d+)", robot)
    ri, ci, rs, cs = int(match.group("rn")), int(match.group("cn")), int(match.group("rs")), int(match.group("cs"))
    ri, ci = (ri + rs * seconds) % rows, (ci + cs * seconds) % cols

    if (ri, ci) not in positions:
        positions[(ri, ci)] = 1
    else:
        positions[(ri, ci)] += 1

for k, v in positions.items():
    if k[0] == rows // 2 and k[1] == cols // 2: continue
    if k[0] < rows // 2 and k[1] < cols // 2: q1 += v
    if k[0] < rows // 2 and k[1] > cols // 2: q2 += v
    if k[0] > rows // 2 and k[1] < cols // 2: q3 += v
    if k[0] > rows // 2 and k[1] > cols // 2: q4 += v

print(f"Factor: {q1*q2*q3*q4}")
