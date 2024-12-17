import aocd
import re

f = aocd.get_data(day=13, year=2024)

machines = [m for m in f.split("\n\n")]
price = 0

for m in machines:
    l1, l2, l3 = [l for l in m.splitlines()]
    match = re.match("Button A: X\\+(?P<ax>\\d+), Y\\+(?P<ay>\\d+)", l1)
    ax, ay = int(match.group("ax")), int(match.group("ay"))
    match = re.match("Button B: X\\+(?P<bx>\\d+), Y\\+(?P<by>\\d+)", l2)
    bx, by = int(match.group("bx")), int(match.group("by"))
    match = re.match("Prize: X=(?P<x>\\d+), Y=(?P<y>\\d+)", l3)
    x, y = int(match.group("x")) + 10000000000000, int(match.group("y")) + 10000000000000

    if (by * x - bx * y) % (ax * by - ay * bx) == 0 and (ax * y - ay * x) % (ax * by - ay * bx) == 0:
        a = (by * x - bx * y) / (ax * by - ay * bx)
        b = (ax * y - ay * x) / (ax * by - ay * bx)
        price += int(a * 3 + b)

print(f"Price is: {price}.")
