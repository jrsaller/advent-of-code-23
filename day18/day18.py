import shared

def intercepts(point, corners):
    inside = False
    y, x = point
    for i in range(len(corners)-1):
        yi, xi = corners[i]
        yj, xj = corners[i+1]
        intersect = ((yi>y) != (yj>y)) and (x < (xj-xi)*(y-yi)/(yj-yi)+xi)
        if intersect:
            inside = not inside
    return inside

def Shoelace(vertices,total):
  #A function to apply the Shoelace algorithm
#   print(vertices)
  numberOfVertices = len(vertices)
  sum1 = 0
  sum2 = 0
  
  for i in range(0,numberOfVertices-1):
    sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
    sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  
  #Add xn.y1
  sum1 = sum1 + vertices[numberOfVertices-1][1]*vertices[0][0]   
  #Add x1.yn
  sum2 = sum2 + vertices[0][1]*vertices[numberOfVertices-1][0]   
  
  area = abs(sum1 - sum2) / 2
  return int(total+area)

def Part1(lines):
    corners = [(0,0)]
    filled = 1
    for line in lines:
        d, dist, _ = line.split()
        match d:
            case 'R':
                corners.append((corners[-1][0], corners[-1][1]+(int(dist))))
                filled+=(int(dist))
            case 'L':
                corners.append((corners[-1][0], corners[-1][1]-int(dist)))
            case 'D':
                corners.append((corners[-1][0]+(int(dist)), corners[-1][1]))
                filled+=(int(dist))
            case 'U':
                corners.append((corners[-1][0]-int(dist), corners[-1][1]))
    min_height = min(corners, key=lambda x: x[0])[0]
    max_height = max(corners, key=lambda x: x[0])[0]
    min_width = min(corners, key=lambda x: x[1])[1]
    max_width = max(corners, key=lambda x: x[1])[1]
    print("MinHeight:", min_height, "maxHeight:", max_height,"minWidth:", min_width,"maxWidth:", max_width)
    origin = (-min_height, -min_width)
    corners = [(y+origin[0], x+origin[1]) for y, x in corners]



    print('---------111111111111-------------:' , Shoelace(corners,filled))


def Part2(lines):
    corners2 = [(0,0)]
    filled2 = 1
    for line in lines:
        _,_,color = line.split()
        color = color[1:-1]
        dist2 = int(color[1:-1],16)
        match color[-1]:
            case '0':
                corners2.append((corners2[-1][0], corners2[-1][1]+int(dist2)))
                filled2+=(int(dist2))
            case '2':
                corners2.append((corners2[-1][0], corners2[-1][1]-int(dist2)))
            case '1':
                corners2.append((corners2[-1][0]+int(dist2), corners2[-1][1]))
                filled2+=(int(dist2))
            case '3':
                corners2.append((corners2[-1][0]-int(dist2), corners2[-1][1]))
    min_height2 = min(corners2, key=lambda x: x[0])[0]
    max_height2 = max(corners2, key=lambda x: x[0])[0]
    min_width2 = min(corners2, key=lambda x: x[1])[1]
    max_width2 = max(corners2, key=lambda x: x[1])[1]
    print("MinHeight:", min_height2, "maxHeight:", max_height2,"minWidth:", min_width2,"maxWidth:", max_width2)
    origin2 = (-min_height2, -min_width2)
    corners2 = [(y+origin2[0], x+origin2[1]) for y, x in corners2]

    print('---------222222222222-------------:' , Shoelace(corners2,filled2))

    

lines = shared.read_file("source.txt")
Part1(lines)
Part2(lines)



# corners2.append((0,0))

# final_map2 = [['.' for _ in range(final_width2)] for _ in range(final_height2)]

# OLD BRUTE FORCE APPROACH
# filled = 0
# for i in range(len(corners)-1):
#     y1, x1 = corners[i]
#     y2, x2 = corners[i+1]

#     # print(y1, x1)
#     for c in range(min(y1,y2), max(y1,y2)):
#         filled+=1
#         final_map[c][x2] = '#'
#     for r in range(min(x1,x2), max(x1,x2)):
#         filled+=1
#         final_map[y2][r] = '#'
#     final_map[y2][x2] = '#'

# print(filled)
# for r, line in enumerate(final_map):
#     # print(line)
#     for c, char in enumerate(line):
#         if char == '.':
#             if intercepts((r,c), corners):
#                 filled += 1
# print(filled)