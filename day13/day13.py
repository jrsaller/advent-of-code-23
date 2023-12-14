import shared

def find_vert_inflect(grid, part=1):
    pos_inflections = []
    for i in range(1,len(grid)):
        top = grid[:i][::-1]
        bottom = grid[i:i+i]  
        # print('top   ',top)
        # print('bottom', bottom)
        if part == 1 and top[:len(bottom)] == bottom:
            return i
        elif part == 2:
            diff_count = 0
            for j in range(len(top[:len(bottom)])):
                diff_count += sum(1 for a, b in zip(top[j], bottom[j]) if a != b)
            if diff_count == 1:
                return i
        # print()
    return -1

def convert_grid(grid):
    new_grid = [''] * len(grid[0])
    for line in grid:
        for i in range(len(line)):
            new_grid[i] += line[i]
    return new_grid

lines = shared.read_file_split('source.txt')
grids = [x.split("\n") for x in lines]
print(grids)

total1 = 0
total2 = 0
for grid in grids:
    print(grid)
    rotated_grid = convert_grid(grid)
    print('PART 1')
    vert_inflect = -1
    horiz_inflect = -1
    vert_inflect = find_vert_inflect(grid)
    if vert_inflect == -1:
        horiz_inflect = find_vert_inflect(rotated_grid)

    print("\tVERT:", vert_inflect)
    print("\tHORIZ:",horiz_inflect)
    if vert_inflect != -1:
        total1 += (vert_inflect * 100)
    elif horiz_inflect != -1:
        total1 += horiz_inflect

    print('PART 2')
    vert_inflect = -1
    horiz_inflect = -1

    vert_inflect = find_vert_inflect(grid, part=2)
    if vert_inflect == -1:
        horiz_inflect = find_vert_inflect(rotated_grid, part=2)
    print("\tVERT:", vert_inflect)
    print("\tHORIZ:",horiz_inflect)
    if vert_inflect != -1:
        total2 += (vert_inflect * 100)
    elif horiz_inflect != -1:
        total2 += horiz_inflect

    print()

print('Part 1 total =',total1)
print('Part 2 total =',total2)