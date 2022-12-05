# --- Day 1: Calorie Counting ---
# elfves' inventory separated by blank lines
# Part 1: most calories by each elf total?
# Part 2: total of top 3 calories
import sys

fname = sys.argv[1]
calories_per_elf = []
with open(fname, 'r') as f:
    cal_curr_elf = 0
    for i,line in enumerate(f):
        if line != '\n':
            cal_curr_elf += int(line.strip('\n'))
        else:
            # next elf
            calories_per_elf.append(cal_curr_elf)
            cal_curr_elf = 0 # reset value

    calories_per_elf.append(cal_curr_elf) # calories of last elf

print(f"Part 1: {max(calories_per_elf)}")
print(f"Part 2: {sum(sorted(calories_per_elf, reverse=True)[:3])}")