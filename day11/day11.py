import re
import sys

import shared

part = sys.argv[1]

lines = shared.read_file('source.txt')

empty_rows = [False] * len(lines[0])
empty_cols = [True] * len(lines)
stars = []

for y, line in enumerate(lines):
    star_locations = [m.start() for m in re.finditer('#', line)]
    # print(star_locations)
    if star_locations == []:
        empty_rows[y] = True
    for location in star_locations:
        stars.append((y,location))
        empty_cols[location] = False
# print(stars)
# print(empty_rows)
# print(empty_cols)
steps = 0

for i in range(len(stars)-1):
    for j in range(i+1,len(stars)):
        # print(stars[i],'=>',stars[j])
        for r in range(min(stars[i][0],stars[j][0]),max(stars[i][0],stars[j][0])):
            if empty_rows[r]:
                if part == '1':
                    steps+=2
                elif part == '2':
                    steps+=1000000
            else:
                steps+=1
        for c in range(min(stars[i][1],stars[j][1]),max(stars[i][1],stars[j][1])):
            if empty_cols[c]:
                if part == '1':
                    steps+=2
                elif part == '2':
                    steps+=1000000
            else:
                steps+=1
print('PART',part, steps)

# Uncomment to see what the final chart looks like, after expansion
# final_lines = []
# for y, line in enumerate(lines):
#     next_line = ''
#     for x,char in enumerate(line):
#         next_line += char
#         if empty_cols[x]:
#             next_line += '.'
#     final_lines.append(next_line)
#     if empty_rows[y]:
#         final_lines.append(next_line)

# for line in final_lines:
#     print(line)
# for star in stars:
