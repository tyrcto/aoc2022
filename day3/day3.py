# --- Day 3: Rucksack Reorganization ---
import sys

def get_pri(ch):
    o = ord(ch)
    if o < ord('a'):
        return o-38
    return o-96

fname = sys.argv[1]
rucksacks = []
with open(fname, 'r') as f:
    rucksacks = f.read().split('\n')

same = []
for line in rucksacks:
    halfsz = len(line)//2
    item1, item2 = set(line[:halfsz]), set(line[halfsz:])
    same.append(item1.intersection(item2).pop())
print("Part 1", sum((list(map(get_pri, same)))))

same2 = []
for i in range(0, len(rucksacks), 3):
    s1, s2, s3 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
    same2.append(s1.intersection(s2).intersection(s3).pop())
# print(same2)
print("Part 2", sum(list(map(get_pri, same2))))