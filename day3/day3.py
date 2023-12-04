import shared
import functools

def get_number_indeces(line: str):
    d = []
    in_number=False
    start = 0
    end = 0
    for index,char in enumerate(line):
        if char.isnumeric():
            if not in_number:
                start = index
                in_number = True
        else:
            if in_number:
                in_number=False
                end=index
                d.append({'val': line[start:end], 'start':start, 'end':end})

    return d

def get_gear_indeces(line):
    return [i for i in range(len(line)) if line.startswith('*', i)]

def get_nearby_text(lines, line_index,check_start,check_end):
    t = ''
    # check line above
    if line_index-1 >= 0:
        t += lines[line_index-1][check_start:check_end].strip()
    # check current line
    t += lines[line_index][check_start:check_end].strip()
    #check next line
    if line_index+1 < len(lines):
        t += lines[line_index+1][check_start:check_end].strip()
    return t
        
def near_symbol(lines, line_index, item):
    check_start = item['start']-1
    check_end = item['end'] + 1
    check_text = ""
    if item['start'] == 0:
        check_start = item['start']
    if item['end'] == len(lines[line_index]):
        check_end = item['end']
    check_text = get_nearby_text(lines, line_index, check_start, check_end)
    return not check_text.strip('.').isalnum() 
    
def check_for_overlap(numbers,spot,adjacent_nums):
    for num in numbers:
        if num['start'] in range(spot-1,spot+2) or num['end']-1 in range(spot-1,spot+2):
            # print('WE GOT A MATCH')
            adjacent_nums.append(int(num['val']))

if __name__ == '__main__':
    lines = shared.read_file('source.txt')
    total = 0
    coords = []
    for i, line in enumerate(lines):
        indeces = get_number_indeces(line)
        #PART 1
        for key in indeces:
            if near_symbol(lines, i, key):
                total+= int(key['val'])
        #PART 2
        gear_locations = get_gear_indeces(line)
        coords.append({'numbers': indeces, 'gears':gear_locations})
    final_sum = 0
    for l, c in enumerate(coords):

        for spot in c['gears']:
            adjacent_nums = []
            
            if l-1 >= 0:
                # print('LINE BEFORE')
                check_for_overlap(coords[l-1]['numbers'],spot,adjacent_nums)
            
            # print('LINE ON')
            check_for_overlap(coords[l]['numbers'],spot,adjacent_nums)
            
            if l+1 < len(coords):
                # print('LINE AFTER')
                check_for_overlap(coords[l+1]['numbers'],spot,adjacent_nums)

            if len(adjacent_nums) == 2:
                product = functools.reduce(lambda a, b: a*b, adjacent_nums)
                final_sum += product

    print('PART 1', total)
    print("PART 2", final_sum)
