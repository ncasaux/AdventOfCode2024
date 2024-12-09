import aocd


def combine(expected_total, so_far_total, remaining_numbers):
    if len(remaining_numbers) == 0:
        if expected_total == so_far_total:
            return True
    else:
        if combine(expected_total, so_far_total + remaining_numbers[0], remaining_numbers[1:]):
            return True
        if combine(expected_total, so_far_total * remaining_numbers[0], remaining_numbers[1:]):
            return True


f = aocd.get_data(day=7, year=2024)
line = f.split("\n\n")[0].splitlines()
total = 0

for l in line:
    expectedTotal = int(l.split(":")[0])
    soFarTotal = int(l.split(":")[1].split()[0])
    remainingNumbers = [int(i) for i in l.split(":")[1].split()[1:]]
    if combine(expectedTotal, soFarTotal, remainingNumbers): total += expectedTotal

print(f"Total is: {total}")
