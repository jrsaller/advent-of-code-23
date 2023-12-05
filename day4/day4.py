import shared

def check_for_wins(win_nums: list,my_nums: list):
    total = 0
    for num in win_nums:
        total += my_nums.count(num)
    return total


if __name__ == '__main__':
    lines = shared.read_file('source.txt')
    score_total = 0
    copies = [1]*len(lines)
    for index, line in enumerate(lines):
        # GET NUMBER LISTS
        line = line.strip()
        split = line.split('|')
        win_nums = split[0].strip().split(':')[1].split(' ')
        win_nums = [x for x in win_nums if x]
        my_nums = split[1].strip().split(' ')
        my_nums = [y for y in my_nums if y]

        wins = check_for_wins(win_nums,my_nums) 
        for win in range(wins):
            copies[index+1+win] += copies[index]
        score = 0
        if wins > 0:
            score = 2 ** (check_for_wins(win_nums,my_nums)-1)
        score_total += score
    print('PART 1',score_total)
    print('PART 2', sum(copies))