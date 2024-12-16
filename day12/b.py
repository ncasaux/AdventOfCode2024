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
g = "." * (2 + len(f.splitlines()[0])) + "\n"
for currentLine in f.splitlines(): g += "." + currentLine + "." + "\n"
g += "." * (2 + len(f.splitlines()[0]))

grid = [[*l] for l in g.splitlines()]
rn, cn = len(grid), len(grid[0])
regions = []
seenPlots = set()
price = 0

for r in range(rn):
    for c in range(cn):
        if (r, c) not in seenPlots and grid[r][c] != '.': regions.append(build_region((r, c), set()))

for region in regions:
    corner = 0
    for plot in region:
        pr, pc = plot[0], plot[1]
        p = grid[pr][pc]
        if grid[pr - 1][pc] != p and grid[pr][pc - 1] != p: corner += 1  # top left corner
        if grid[pr - 1][pc] != p and grid[pr][pc + 1] != p: corner += 1  # top right corner
        if grid[pr][pc - 1] != p and grid[pr + 1][pc] != p: corner += 1  # bottom left corner
        if grid[pr][pc + 1] != p and grid[pr + 1][pc] != p: corner += 1  # bottom right corner
        if grid[pr][pc + 1] == p and grid[pr + 1][pc] == p and grid[pr + 1][pc + 1] != p: corner += 1
        if grid[pr][pc - 1] == p and grid[pr + 1][pc] == p and grid[pr + 1][pc - 1] != p: corner += 1
        if grid[pr - 1][pc] == p and grid[pr][pc + 1] == p and grid[pr - 1][pc + 1] != p: corner += 1
        if grid[pr - 1][pc] == p and grid[pr][pc - 1] == p and grid[pr - 1][pc - 1] != p: corner += 1
    price += corner * len(region)

print(f"Total price: {price}.")
