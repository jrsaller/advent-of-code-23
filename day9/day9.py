import shared

def getNextNumber(history):
    if len(set(history)) == 1:
        return history[0]
    else:
        diffList = [history[i+1]-history[i] for i in range(len(history)-1)]
        nextNum = getNextNumber(diffList)
        return history[-1] + nextNum

total = 0
reverse_total = 0
lines = shared.read_file('source.txt')
for line in lines:
    line = [int(l) for l in line.split()]
    # print(line)
    nextNum = getNextNumber(line)
    line.reverse()
    nextNum2 = getNextNumber(line)
    # print(nextNum)
    # print(nextNum2)
    total += nextNum
    reverse_total += nextNum2
print('PART 1', total)
print('PART 2', reverse_total)
