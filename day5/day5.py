#--- Day 5: Supply Stacks ---
import sys

commands = []
with open(sys.argv[1], 'r') as f:
    lines = f.read().split('\n')
    temp_stack, commands = lines[:lines.index('')], lines[lines.index('')+1:]

# Crate stacks setup
n_stack = len([i for i in temp_stack[-1] if i != ' '])
stacks = [None]*n_stack
for lvl in temp_stack[:-1]:
    # check which stack the crate is on
    i = 0
    while i < len(lvl):
        c = lvl[i]
        if ' ' != c:
            st_num = i//4
            # print('\nst',st_num)
            if stacks[st_num] == None:
                stacks[st_num] = [lvl[i+1]]    # place crate in stack n
            else:
                stacks[st_num].append(lvl[i+1])
            # print(stacks)
            i+=2
        i+=1

# parse only integers in command string
def parse_int(s:str):
    check = list(map(str, list(range(0,10))))
    ints = []
    i = 0
    while i < len(s):
        found = False
        try:
            if s[i] in check and s[i+1] in check:   # >=10
                ints.append(int(s[i:i+2]))
                i+=1
                found=True
        except IndexError:
            pass
        if s[i] in check and not found:
            ints.append(int(s[i]))
        i+=1
    return ints

# for part 2 (requires deepcopying)
stacks2 = [[i for i in st] for st in stacks]

# parse commands
for com in commands:
    mv, src, dst = parse_int(com)
    
    # fetch mv amount from stacks[src]
    fetch = []
    fetch2 = []
    for i in range(mv):
        fetch.append(stacks[src-1].pop(0))
        fetch2.append(stacks2[src-1].pop(0))

    # place into stacks[dst]
    for crate in fetch:
        stacks[dst-1].insert(0,crate)

    # for part 2, fetched crates aren't reversed (confusing, i know)
    fetch2.reverse()
    for crate in fetch2:
        stacks2[dst-1].insert(0,crate)

top = []
for s in stacks:
    top.append(s[0])
print("Part 1", ''.join(top))

top2 = []
for s in stacks2:
    top2.append(s[0])
print("Part 2", ''.join(top2))