import shared

UP = 'UP'
RIGHT = 'RIGHT'
DOWN = 'DOWN'
LEFT = 'LEFT'

def findStart(lines):
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if line[j] == 'S':
                return (i,j)
    return (-1,-1)

def findNextPos(char,x,y,from_dir):
    # print(char,x,y,from_dir)
    match char:
        case '|':
            if from_dir == UP:
                return (UP,x,y+1)
            elif from_dir == DOWN:
                return (DOWN,x,y-1)
        case '-':
            if from_dir == LEFT:
                return (LEFT, x+1, y)
            elif from_dir == RIGHT:
                return (RIGHT,x-1,y)
        case 'L':
            if from_dir == UP:
                return LEFT,x+1,y
            elif from_dir == RIGHT:
                return (DOWN,x,y-1)
        case 'J':
            if from_dir == LEFT:
                return (DOWN,x,y-1)
            elif from_dir == UP:
                return (RIGHT,x-1,y)
        case '7':
            if from_dir == LEFT:
                return (UP,x,y+1)
            elif from_dir == DOWN:
                return (RIGHT,x-1,y)
        case 'F':
            if from_dir == RIGHT:
                return (UP,x,y+1)
            elif from_dir == DOWN:
                return (LEFT,x+1,y)

def countSteps(lines, positions, path):
    count = 1
    while not (positions[0][1] == positions[1][1] and positions[0][2] == positions[1][2]):
        from1, x1, y1 = positions[0]
        positions[0] = findNextPos(lines[y1][x1],x1,y1,from1)
        from2, x2, y2 = positions[1]
        positions[1] = findNextPos(lines[y2][x2],x2,y2,from2)
        count+=1
        path.append(positions[0][1:])
        path.append(positions[1][1:])
    return count

def replaceStart(lines,path):
    firstSteps = path[1:3]
    startX = path[0][0]
    startY = path[0][1]
    # F
    if (startX,startY+1) in firstSteps and (startX+1,startY) in firstSteps:
        lines[startY] = lines[startY].replace('S', 'F',1)
    # 7
    if (startX-1,startY) in firstSteps and (startX,startY+1) in firstSteps:
        lines[startY] = lines[startY].replace('S', '7',1)
    # L
    if (startX,startY-1) in firstSteps and (startX+1,startY) in firstSteps:
        lines[startY] = lines[startY].replace('S', 'L',1)
    # J
    if (startX-1,startY) in firstSteps and (startX,startY-1) in firstSteps:
        lines[startY] = lines[startY].replace('S', 'J',1)
    # -
    if (startX-1,startY) in firstSteps and (startX+1,startY) in firstSteps:
        lines[startY] = lines[startY].replace('S', '-',1)
    # |
    if (startX,startY-1) in firstSteps and (startX,startY+1) in firstSteps:
        lines[startY] = lines[startY].replace('S', '|',1)

def getFirstStepOut(lines, x, y):
    positions = []
    # UP
    char1 = lines[y-1][x]
    if char1 in ['|','F','7']:
        positions.append((DOWN, x,y-1))
    # RIGHT
    char2 = lines[y][x+1]
    if char2 in ['-','7','J']:
        positions.append((LEFT, x+1,y))
    # DOWN
    char3 = lines[y+1][x]
    if char3 in ['L','|','J']:
        positions.append((UP, x,y+1))
    # LEFT
    char4 = lines[y][x-1]
    if char4 in ['F','-','L']:
        positions.append((RIGHT, x-1,y))
    return positions

lines = shared.read_file('source.txt')
path = []
# print(lines)
y,x = findStart(lines)
path.append((x,y))
positions = getFirstStepOut(lines,x,y)
path.append(positions[0][1:])
path.append(positions[1][1:])
count = countSteps(lines,positions,path)
print('PART 1', count)

# PART 2
replaceStart(lines,path)

insidePoints = 0
for y, line in enumerate(lines):
    for x in range(len(line)-1):
        hitVertices = 0
        if (x,y) not in path:
            for r in range(x+1, len(line)):
                if (r,y) in path and lines[y][r] in ['L','J','|']:
                    hitVertices += 1
            if hitVertices % 2 == 1:
                insidePoints += 1
print('PART 2', insidePoints)