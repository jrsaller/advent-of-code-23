import shared
import sys

def translate_hand(line, part):
    d = {
        'T': ':',
        'J': ';',
        'Q': '<',
        'K': '=',
        'A': '>',
    }
    if part == 2:
        d['J'] = '/'
    table = str.maketrans(d)
    return line.translate(table)

def determine_score(hand,part):
    counter = {}
    wilds = 0
    max_score = 0
    for char in hand:
        counter[char] = counter.get(char,0) + 1
    print(counter)
    if part == 2:
        if len(counter.values()) > 1 and counter.get('/',0) > 0: 
            wilds = counter.pop('/',0)
            if wilds > 0:
                max_score += wilds
    max_score += max(counter.values())
    if wilds > 0:
        max_score_count = list(counter.values()).count(max_score-wilds)
    else:
        max_score_count = list(counter.values()).count(max_score)
    match max_score:
        case 5:
            # five of a kind
            return 6
        case 4:
            # four of a kind
            return 5
        case 3:
            if (2 in counter.values() and wilds == 0) or (max_score_count == 2 and wilds == 1):
                # full house
                return 4
            else:
                # three of a kind
                return 3
        case 2:
            if max_score_count == 2:
                # two pair
                return 2
            else:
                # one pair
                return 1
        case 1:
            # high card
            return 0
        case _:
            return -1

lines = shared.read_file('source.txt')
part = 1
if sys.argv[-1] == '2':
    part = 2
fives = []
fours = []
fulls = []
threes = []
two_pairs = []
one_pairs = []
highs = []


for line in lines:
    new_line = translate_hand(line,part)
    hand = new_line[:5]
    score = determine_score(hand,part)
    match score:
        case 6:
            fives.append(new_line)
        case 5:
            fours.append(new_line)
        case 4:
            fulls.append(new_line)
        case 3:
            threes.append(new_line)
        case 2:
            two_pairs.append(new_line)
        case 1:
            one_pairs.append(new_line)
        case 0:
            highs.append(new_line)


print('fives:', sorted(fives))
print('fours:',sorted(fours))
print('fulls',sorted(fulls))
print('threes', sorted(threes))
print('two_pairs:',sorted(two_pairs))
print('one_pairs:',sorted(one_pairs))
print('high cards',sorted(highs))

final = sorted(highs) + sorted(one_pairs)+sorted(two_pairs)+sorted(threes)+sorted(fulls)+sorted(fours)+sorted(fives)

total = 0
for rank in range(len(final)):
    total += ((rank+1) * int(final[rank][6:]))
print('PART',part,total)