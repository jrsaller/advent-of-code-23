import shared
import functools
import math

lines = shared.read_file('source.txt')
times = [int(x) for x in lines[0].strip().split()[1:]]
print('times',times)
records = [int(x) for x in lines[1].strip().split()[1:]]
print('records',records)

all_wins = []
for index, time in enumerate(times):
    wins1 = (time + math.sqrt((time ** 2) - (4 * records[index]))) / (2)
    wins2 = (time - math.sqrt((time ** 2) - (4 * records[index]))) / (2)
    low_number = min(wins1,wins2)
    print('answer',time-(2*math.ceil(low_number))+1)
    all_wins.append(time-(2*math.ceil(low_number))+1)
print('PART 1', functools.reduce(lambda a,b: a*b,all_wins))

# PART 2
mega_time = int(functools.reduce(lambda a,b: str(a)+str(b),times))
mega_record = int(functools.reduce(lambda a,b: str(a)+str(b),records))

bigwins1 = (mega_time + math.sqrt((mega_time ** 2) - (4 * mega_record))) / (2)
bigwins2 = (mega_time - math.sqrt((mega_time ** 2) - (4 * mega_record))) / (2)
low_number = min(bigwins1,bigwins2)
print('PART 2',mega_time-(2*math.ceil(low_number))+1)

# wins = 0
# for i in range(1, mega_time//2):
#     if i * (mega_time-i) > mega_record:
#         wins+=1
# wins *=2
# wins += (2 **(mega_time % 2))
# print("PART 2",wins)
