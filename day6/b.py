import copy
import aocd

f = aocd.get_data(day=6, year=2024)


def looping(p_grid, p_starting_position, p_starting_cap):
    _positions = set()
    curr_pos = p_starting_position
    curr_cap = p_starting_cap
    _positions.add((curr_pos, curr_cap))
    while 0 <= curr_pos.real + curr_cap.real <= len(p_grid) - 1 and 0 <= -(curr_pos.imag + curr_cap.imag) <= len(
            p_grid[0]) - 1:
        if p_grid[-int(curr_pos.imag + curr_cap.imag)][int(curr_pos.real + curr_cap.real)] == "#":  # rock ahead
            curr_cap *= complex(0, -1)
        else:
            curr_pos += curr_cap
        if (curr_pos, curr_cap) in _positions:
            return True
        _positions.add((curr_pos, curr_cap))
    return False


positions = set()
obstacles = set()

grid = [[*l] for l in f.splitlines()]

currPos = complex(f.find("^") % (len(grid[0]) + 1), -(f.find("^") // (len(grid[0]) + 1)))
currCap = complex(0, 1)

positions.add(currPos)
while 0 <= currPos.real + currCap.real <= len(grid) - 1 and 0 <= -(currPos.imag + currCap.imag) <= len(grid[0]) - 1:
    if grid[-int(currPos.imag + currCap.imag)][int(currPos.real + currCap.real)] == "#":  # rock ahead
        currCap *= complex(0, -1)
    else:
        if (currPos + currCap) not in positions:
            updatedGrid = copy.deepcopy(grid)
            updatedGrid[-int(currPos.imag + currCap.imag)][int(currPos.real + currCap.real)] = "#"
            if looping(updatedGrid, currPos, currCap):
                obstacles.add(currPos + currCap)

        currPos += currCap
        positions.add(currPos)

print(f"Possible obstacles: {len(obstacles)}.")
