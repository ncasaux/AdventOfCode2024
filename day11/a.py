import aocd

f = aocd.get_data(day=11, year=2024)
l = [int(i) for i in f.split()]

for i in range(25):
    m = []
    for n in l:
        if int(n) == 0:
            m.append(1)
            continue
        if len(str(n)) % 2 == 0:
            m.append(int(str(n)[:int(len(str(n)) // 2)]))
            m.append(int(str(n)[len(str(n)) // 2:]))
            continue
        m.append(n * 2024)
    l = m

print(f"Number of stones: {len(l)}.")
