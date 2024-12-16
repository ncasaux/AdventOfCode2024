def build_region(p_plot: tuple, p_region: set):
    p_region.add(p_plot)
    pr, pc = p_plot[0], p_plot[1]
    if 0 <= pr - 1 <= rn - 1 and grid[pr - 1][pc] == grid[pr][pc] and (pr - 1, pc) not in p_region:
        p_region = build_region((pr - 1, pc), p_region)
    if 0 <= pr + 1 <= rn - 1 and grid[pr + 1][pc] == grid[pr][pc] and (pr + 1, pc) not in p_region:
        p_region = build_region((pr + 1, pc), p_region)
    if 0 <= pc - 1 <= cn - 1 and grid[pr][pc - 1] == grid[pr][pc] and (pr, pc - 1) not in p_region:
        p_region = build_region((pr, pc - 1), p_region)
    if 0 <= pc + 1 <= cn - 1 and grid[pr][pc + 1] == grid[pr][pc] and (pr, pc + 1) not in p_region:
        p_region = build_region((pr, pc + 1), p_region)
    seenPlots.add((pr, pc))
    return p_region


import aocd

f = aocd.get_data(day=12, year=2024)
grid = [[*l] for l in f.splitlines()]
rn, cn = len(grid), len(grid[0])
regions = []
seenPlots = set()
price = 0

for r in range(rn):
    for c in range(cn):
        if (r, c) not in seenPlots: regions.append(build_region((r, c), set()))

for region in regions:
    perimeter = 0
    for coord in region:
        sides = 4
        if (coord[0] - 1, coord[1]) in region: sides -= 1
        if (coord[0] + 1, coord[1]) in region: sides -= 1
        if (coord[0], coord[1] - 1) in region: sides -= 1
        if (coord[0], coord[1] + 1) in region: sides -= 1
        perimeter += sides
    price += perimeter * len(region)

print(f"Total price: {price}.")
