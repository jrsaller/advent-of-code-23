import shared

line = shared.read_file('source.txt')[0]
line = line.split(',')
scores_1 = []
boxes_2 = [ [] for _ in range(256) ]

for item in line:
    # PART 1
    total1 = 0
    for char in item:
        total1 += ord(char)
        total1 *= 17
        total1 %= 256
    scores_1.append(total1)
    
    # PART 2
    total2 = 0
    equal_location = item.find('=')
    end_label = equal_location if equal_location != -1 else item.find('-')
    label = item[:end_label]
    if equal_location != -1:
        value = item[equal_location + 1]
    
    for char in label:
        total2 += ord(char)
        total2 *= 17
        total2 %= 256
    if equal_location != -1:
        location = -1
        for s, item in enumerate(boxes_2[total2]):
            if item[0] == label:
                location = s
                break
        if location != -1:
            boxes_2[total2][location] = [label, value]
        else:
            boxes_2[total2].append([label, value])
    else:
        # THERE WAS A MINUS SIGN
        location = -1
        for s, item in enumerate(boxes_2[total2]):
            if item[0] == label:
                location = s
                break
        if location != -1:
            boxes_2[total2].pop(location)

print(scores_1)
print('Part 1' , sum(scores_1))
print()
# [print(item) for item in boxes_2]
final_focal_length = 0
for i,box in enumerate(boxes_2):
    for spot, item in enumerate(box):
        final_focal_length += ((1 + i) * (spot+1) * (int(item[1])))
print('Part 2', final_focal_length) 