import aocd

f = aocd.get_data(day=6, year=2024)

positions = set()

cap = complex(0, 1)
grid = f.splitlines()
currPos = complex(f.find("^") % (len(grid[0]) + 1), -(f.find("^") // (len(grid[0]) + 1)))

positions.add(currPos)
while 0 <= currPos.real + cap.real <= len(grid) - 1 and 0 <= -(currPos.imag + cap.imag) <= len(grid[0]) - 1:
    if grid[-int(currPos.imag + cap.imag)][int(currPos.real + cap.real)] == "#":  # rock ahead
        cap *= complex(0, -1)
    else:
        currPos += cap
        positions.add(currPos)

print(f"Unique positions: {len(positions)}.")
