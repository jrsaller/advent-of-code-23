import shared
import re

def convert_grid(grid):
    new_grid = [''] * len(grid[0])
    for line in grid:
        for i in range(len(line)):
            new_grid[i] += line[i]
    return new_grid

def shift(grid, dir='L'):
    new_grid = [''] * len(grid[0])
    for n, line in enumerate(grid):
        if dir == 'R':
            line = line[::-1]
        squares = [m.start() for m in re.finditer('#',line)] + [len(line)]
        rocks = line.count('O', 0, squares[0])
        new_grid[n] += 'O' * rocks
        while len(new_grid[n]) < squares[0]:
            new_grid[n] += '.'
        for p in range(len(squares)-1):
            new_grid[n] += '#'
            min_pos = squares[p]
            max_pos = squares[p+1]
            rocks = line.count('O', min_pos, max_pos)
            new_grid[n] += 'O' * rocks
            while len(new_grid[n]) < max_pos:
                new_grid[n] += '.'
        if dir == 'R':
            new_grid[n] = new_grid[n][::-1]
    # print(new_grid)
    return new_grid

# def calc_north_support_load(grid):
#     total = 0
#     for c in grid:
#         squares = [m.start() for m in re.finditer('#',c)]
#         squares = squares + [len(c)]
#         print(c, '=>', squares)
#         rocks = c.count('O', 0, squares[0])
#         for r in range(rocks):
#             # print('r',r)
#             sub = len(c)-r
#             # print('sub',sub)
#             total += sub
#         for p in range(len(squares)-1):
#             min_pos = squares[p]
#             max_pos = squares[p+1]
#             # print(c[min_pos:max_pos])
#             rocks = c.count('O', min_pos, max_pos)
#             # print(rocks,'[',min_pos,max_pos,']')
#             for r in range(1,rocks+1):
#                 # print('r',r)
#                 sub = len(c)-(min_pos+r)
#                 # print('sub',sub)
#                 total += sub
#     return total

def calc_north_support_load_v2(grid):
    total = 0
    for i, line in enumerate(grid):
        for char in line:
            if char == 'O':
                total += len(grid) - i
    return total

# Facing north
cols = shared.read_file('source.txt')
# print('Part 1', calc_north_support_load(cols))
print('Part 1', calc_north_support_load_v2(convert_grid(shift(convert_grid(cols), dir='L'))))

for i in range(1000):
    # NORTH
    cols = convert_grid(shift(convert_grid(cols),dir='L'))
    # WEST
    cols = shift(cols,dir='L')
    # SOUTH
    cols =convert_grid(shift(convert_grid(cols), dir='R'))
    # EAST
    cols = shift(cols, dir='R')

for line in cols:
    print(line)

print('Part 2', calc_north_support_load_v2(cols))