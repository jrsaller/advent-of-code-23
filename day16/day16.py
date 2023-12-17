import shared

LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'

def display_map(lines):
    for line in lines:
        print(line)

def explore_map2(lines,todo):
    done = []
    while todo:
        pos,from_dir = todo.pop()
        if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
            continue
        while (pos,from_dir) not in done:
            done.append((pos,from_dir))
            match lines[pos[0]][pos[1]]: # y,x
                case '|':
                    match from_dir:
                        case 'UP':
                            todo.append(((pos[0]+1, pos[1]), UP))
                        case 'DOWN':
                            todo.append(((pos[0]-1, pos[1]), DOWN))
                        case 'LEFT' | 'RIGHT':
                            todo.append(((pos[0]-1, pos[1]), DOWN))
                            todo.append(((pos[0]+1, pos[1]), UP))
                case '-':
                    match from_dir:
                        case 'LEFT':
                            todo.append(((pos[0], pos[1]+1), LEFT))
                        case 'RIGHT':
                            todo.append(((pos[0], pos[1]-1), RIGHT))
                        case 'UP' | 'DOWN':
                            todo.append(((pos[0], pos[1]+1), LEFT))
                            todo.append(((pos[0], pos[1]-1), RIGHT))
                case '/':
                    match from_dir:
                        case 'LEFT':
                            todo.append(((pos[0]-1, pos[1]), DOWN))
                        case 'RIGHT':
                            todo.append(((pos[0]+1, pos[1]), UP))
                        case 'UP':
                            todo.append(((pos[0], pos[1]-1), RIGHT))
                        case 'DOWN':
                            todo.append(((pos[0], pos[1]+1), LEFT))
                case '\\':
                    match from_dir:
                        case 'LEFT':
                            todo.append(((pos[0]+1, pos[1]), UP))
                        case 'RIGHT':
                            todo.append(((pos[0]-1, pos[1]), DOWN))
                        case 'UP':
                            todo.append(((pos[0], pos[1]+1), LEFT))
                        case 'DOWN':
                            todo.append(((pos[0], pos[1]-1), RIGHT))
                case _:
                    match from_dir:
                        case 'LEFT':
                            todo.append(((pos[0], pos[1]+1), from_dir))
                        case 'RIGHT':
                            todo.append(((pos[0], pos[1]-1), from_dir))
                        case 'UP':
                            todo.append(((pos[0]+1, pos[1]), from_dir))
                        case 'DOWN':
                            todo.append(((pos[0]-1, pos[1]), from_dir))
    return [item[0] for item in done]


lines = shared.read_file('source.txt')

todo = [[(0,0),LEFT]]

scores = []

for x in range(len(lines[0])):
    print('EXPLORING 0',x)
    done = explore_map2(lines, [[(0,x),UP]])
    final2 = []
    for item in done:
        if item not in final2:
            final2.append(item)
    scores.append(len(final2))

    print('EXPLORING',len(lines)-1,x)
    done = explore_map2(lines, [[(len(lines)-1,x),DOWN]])
    final2 = []
    for item in done:
        if item not in final2:
            final2.append(item)
    scores.append(len(final2))

for y in range(len(lines)):
    print('EXPLORING',y,0)
    done = explore_map2(lines, [[(y,0),LEFT]])
    final2 = []
    for item in done:
        if item not in final2:
            final2.append(item)
    scores.append(len(final2))

    print('EXPLORING',y,len(lines[0])-1)
    done = explore_map2(lines, [[(y,len(lines[0])-1),RIGHT]])
    final2 = []
    for item in done:
        if item not in final2:
            final2.append(item)
    scores.append(len(final2))

display_map(lines)

done = explore_map2(lines, todo)
final1 = []
for item in done:
    if item not in final1:
        final1.append(item)
print('PART 1: ', len(final1))
print('PART 2:', max(scores))