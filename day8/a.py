import aocd

f = aocd.get_data(day=8, year=2024)

grid = [[*l] for l in f.splitlines()]
antennas = {}
antinodes = set()

rn = len(grid)
cn = len(grid[0])

for r in range(rn):
    for c in range(cn):
        if grid[r][c] != ".":
            if grid[r][c] not in antennas:
                antennas[grid[r][c]] = [(r, c)]
            else:
                antennas[grid[r][c]].append((r, c))

for k, v in antennas.items():
    for l in range(len(v)):
        for r in range(l + 1, len(v)):
            vlr, vlc, vrr, vrc = v[l][0], v[l][1], v[r][0], v[r][1]
            dr, dc = vrr - vlr, vrc - vlc
            if 0 <= vlr - dr <= rn - 1 and 0 <= vlc - dc <= cn - 1:
                antinodes.add((vlr - dr, vlc - dc))
            if 0 <= vrr + dr <= rn - 1 and 0 <= vrc + dc <= cn - 1:
                antinodes.add((vrr + dr, vrc + dc))

print(f"Unique antinodes: {len(antinodes)}")
