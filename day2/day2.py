# python day2.py 1 for PART 1, - 2685
# python day2.py 2 for PART 2 - 83707

import os
import sys

def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()
    
def break_into_games(lines):
    l=[]
    for line in lines:
        rounds = line.split(':')[1].strip()
        l.append(rounds.split(';'))
    return l

def count_round(round: str):
    r = 0
    g = 0
    b = 0
    color_count = round.split(',')
    for item in color_count:
        if item.find('red') > 0:
            r = int(item.split('red')[0])
        if item.find('green') > 0:
            g = int(item.split('green')[0])
        if item.find('blue') > 0:
            b = int(item.split('blue')[0])
    return r, g, b
    
def init(part2):
    filename = os.path.join(sys.path[0], "source.txt")
    lines = read_file(filename)
    games = break_into_games(lines)
    if part2:
        final_total = 0

        for index, game in enumerate(games):
            red_min = 0
            green_min = 0
            blue_min = 0

            print('\nGAME', index+1)

            for round in game:
                print(round)
                r,g,b = count_round(round)
                print('redcount:', r, 'greencount:', g, 'bluecount:', b)
                if r > red_min:
                    print('update red to', r)
                    red_min = r
                if g > green_min:
                    print('update green to', g)
                    green_min = g
                if b > blue_min:
                    print('update blue to', b)
                    blue_min = b
            print('red_min:', red_min, 'green_min:', green_min, 'blue_min:', blue_min)
            final_total += (red_min * green_min * blue_min)
        print(final_total)

    else:
        red_max = 12
        green_max = 13
        blue_max = 14
        win_total = 0

        for index, game in enumerate(games):
            print('\nGAME', index+1)
            round_fail = False
            for round in game:
                print(round)
                r,g,b = count_round(round)
                print('redcount:',r,'greencount:',g,'bluecount:',b)
                if r > red_max or g > green_max or b > blue_max:
                    round_fail = True
                    break

            if not round_fail:
                win_total += (index+1)

        print(win_total)
                
    
if __name__ == "__main__":
    init(sys.argv[1]=="2")