import shared
import math

def create_map(lines):
    d = {}
    for line in lines:
        div = [x.strip() for x in line.split('=')]
        LR = div[1].split(',')
        L = LR[0][1:].strip()
        R = LR[1][:-1].strip()
        d[div[0]] = {'L':L,'R':R}
    return d

def calculate_steps(directions, map, start_pos, end_pos):
    step = 0
    pos = start_pos
    while pos != end_pos:
        pos = map[pos][directions[step%len(directions)]]
        step += 1
    return step

# PART 1
lines = shared.read_file('source.txt')
directions = lines[0]
pos = 'AAA'
map = create_map(lines[2:])

print('PART 1', calculate_steps(directions, map,'AAA','ZZZ'))

# PART 2
super_pos = []
for key in map:
    if key[-1] == 'A':
        super_pos.append(key)
print(super_pos)
steps = [0] * len(super_pos)
for index, pos in enumerate(super_pos):
    while not pos.endswith('Z'):
        pos = map[pos][directions[steps[index]%len(directions)]]
        steps[index]+=1
print(steps)
print('PART 2',math.lcm(*steps))