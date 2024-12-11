def build_path(p_path: list, p_score: set):
    lp = p_path[-1]
    lpr, lpc = lp[0], lp[1]
    v = int(grid[lpr][lpc])
    if v == 9:
        p_score.add(lp)
    if lpr > 0 and grid[lpr - 1][lpc] != "." and int(grid[lpr - 1][lpc]) == v + 1:
        p_score = build_path(p_path + [(lpr - 1, lpc)], p_score)
    if lpr < rows - 1 and grid[lpr + 1][lpc] != "." and int(grid[lpr + 1][lpc]) == v + 1:
        p_score = build_path(p_path + [(lpr + 1, lpc)], p_score)
    if lpc > 0 and grid[lpr][lpc - 1] != "." and int(grid[lpr][lpc - 1]) == v + 1:
        p_score = build_path(p_path + [(lpr, lpc - 1)], p_score)
    if lpc < cols - 1 and grid[lpr][lpc + 1] != "." and int(grid[lpr][lpc + 1]) == v + 1:
        p_score = build_path(p_path + [(lpr, lpc + 1)], p_score)
    return p_score


import aocd

f = aocd.get_data(day=10, year=2024)

grid = f.splitlines()
rows = len(grid)
cols = len(grid[0])
count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '0':
            count += len(build_path([(r, c)], set()))

print(f"Score: {count}.")
