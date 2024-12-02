import aocd

f = aocd.get_data(day=2, year=2024)

line = []
diffLine = []
safe = 0

for currentLine in f.splitlines():
    line = list(map(int, currentLine.split()))
    diffLine = [line[i+1]-line[i] for i in range(0,len(line)-1)]
    if min(diffLine)>=1 and max(diffLine)<=3 or min(diffLine)>=-3 and max(diffLine)<=-1: safe+=1

print(f"Number of safe reports: {safe}.")