import shared
import functools

@functools.cache
def recurse(line, hints):
    # no more hints
    if len(hints) == 0:
        return 0 if '#' in line else 1
    # no characters left in map
    if len(line) == 0:
        return 1 if len(hints) == 0 else 0

    count = 0

    # if the first character is a dot or question mark(treated as dot),
    # we can move onto the next character, and not count it as part f a broken section
    if line[0] in '.?':
        count += recurse(line[1:], hints)

    # if the first character is a # or a ? (treated as a #)
    if line[0] in '#?':
        # 1. check the length of broken springs from hints can still fit in the line
        # 2. check there's not a dot in the first hints[0] characters (which would break the count)
        # 3. check that hints[0] is exactly the length of the line, or that the next character is not a # (too long a broken chain)
        if hints[0] <= len(line) and '.' not in line[:hints[0]] and (len(line) == hints[0] or line[hints[0]] != '#'):
            count += recurse(line[hints[0]+1:], hints[1:])
    
    return count



lines = shared.read_file('source.txt')
p1, p2 = 0,0

for line in lines:
    split = line.split()
    slots = split[0]
    hints = [int(item) for item in split[1].split(',')]
    p1 += recurse(slots, (springs := tuple(map(int, hints))))
    p2 += recurse('?'.join([slots]*5), springs * 5)

print('Part 1',p1)
print('Part 2',p2)