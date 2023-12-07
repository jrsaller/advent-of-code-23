import shared

def translate_seeds(lines,seeds):
    change_check = [False] * len(seeds)
    for line in lines:
        if ':' not in line:
            nums = line.split(' ')
            nums = [int(x) for x in nums]
            # print(nums)
            seeds_edit = seeds[:]
            for index, seed in enumerate(seeds):
                diff = seed - nums[1]
                if diff < nums[2] and diff >= 0 and not change_check[index]:
                    # print(seed,'=>',nums[0] + diff)
                    seeds_edit[index] = nums[0] + diff
                    change_check[index] = True
            seeds = seeds_edit
        else:
            change_check = [False for x in change_check]
        # print('seeds',seeds)
    return seeds

def translate_seeds_part2(lines,seeds):
    # print(seeds)
    range_count = len(seeds)
    for line in lines:
        if ':' not in line:
            nums = line.split(' ')
            nums = [int(x) for x in nums]
            transform = nums[0] - nums[1]
            # print(nums)
            for index in range(0,range_count,2):
                overlap = range(max(seeds[index],nums[1]),min(seeds[index+1],nums[1]+nums[2]))
                if len(overlap) > 0:
                    if overlap == range(seeds[index],seeds[index+1]):
                        # FULL SWAP OUT
                        seeds.append(seeds[index] + transform)
                        seeds.append(seeds[index+1] + transform)
                        seeds[index] = -1
                        seeds[index+1] =-1
                    else:
                        # print('THERE WAS AN OVERLAP BUT IT WASNT TOTAL')
                        if seeds[index] == min(overlap):
                            # print('the min match')
                            diff = seeds[index] - nums[1]
                            seeds[index] = max(overlap) + 1
                            seeds.append(nums[0] + diff)
                            seeds.append(nums[0] + diff + len(overlap))      
                        elif seeds[index+1] == max(overlap) + 1:
                            # print('the max match')
                            diff = nums[1]-seeds[index+1]
                            seeds[index+1] = min(overlap)
                            seeds.append(nums[0])
                            seeds.append(nums[0] + len(overlap))
                        else:
                            # Overlap is contained WITHIN the current range
                            seeds.insert(index+1, max(overlap)+1)
                            seeds.insert(index+1,min(overlap))
                            seeds.append(nums[0])
                            seeds.append(nums[0] + len(overlap))
        else:
            seeds = [x for x in seeds if x != -1]
            print('End Section seeds',seeds)
            range_count = len(seeds)

    seeds = [x for x in seeds if x != -1]
    return seeds

if __name__ == '__main__':
    lines = shared.read_file('source.txt')
    seeds = lines[0].strip().split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    seed_range = seeds[:]
    for index in range(1, len(seeds),2):
        seed_range[index] += seed_range[index-1]
    content = [x.strip() for x in lines if x.strip() ]
    # print(seeds)
    # print(seed_range)
    seeds = translate_seeds(content,seeds)
    seed_range_final = translate_seeds_part2(content,seed_range[:])
    # print(seeds)
    print('PART 1',min(seeds))
    # print(seed_range)
    # print(seed_range_final)
    print('PART 2',min(seed_range_final))