def process_stones(old_list: list, depth: int):
    global mem
    if depth == 0:
        return len(old_list)
    count = 0
    for n in old_list:
        if (n, depth) in mem:
            v = mem[(n, depth)]
        elif int(n) == 0:
            new_list = [1]
            v = process_stones(new_list, depth - 1)
        elif len(str(n)) % 2 == 0:
            new_list = [int(str(n)[:int(len(str(n)) // 2)]), int(str(n)[len(str(n)) // 2:])]
            v = process_stones(new_list, depth - 1)
        else:
            new_list = [n * 2024]
            v = process_stones(new_list, depth - 1)
        mem[(n, depth)] = v
        count += v
    return count


import aocd

f = aocd.get_data(day=11, year=2024)
l = [int(i) for i in f.split()]
mem = {}

print(f"Number of stones: {process_stones(l, 75)}.")
