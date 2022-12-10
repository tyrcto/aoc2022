# --- Day 9: Rope Bridge ---
# head and tail must always be touching (can be diagonal, overlap)
# How many positions does the tail of the rope visit at least once?
import sys

instructions = []
with open(sys.argv[1], 'r') as f:
    instructions = f.read().splitlines()

def plot(t, h):
    limx = max(t[0], h[0])
    limy = max(t[1], h[1])

    for i in range(limy+1):
        for j in range(limx+1):
            if i == t[1] and j == t[0]:
                print('T', end=' ')
            elif i == h[1] and j == h[0]:
                print('H', end=' ')
            else:
                print('.', end=' ')
        print()

def update_follow(follow, lead):
    diff_x = abs(follow[0]-lead[0])
    diff_y = abs(follow[1]-lead[1])

    if max(diff_x, diff_y) > 1:
        # follow head
        # check same y
        if follow[1] == lead[1]:
            follow[0] += -1 if lead[0]<follow[0] else 1
        # check same x
        elif follow[0] == lead[0]:
            follow[1] += -1 if lead[1]<follow[1] else 1
        # diagonal
        elif follow[0] < lead[0]:
            follow[0] += 1
            if follow[1] < lead[1]:
                follow[1] += 1
            else:
                follow[1] -= 1
        elif follow[0] > lead[0]:
            follow[0] -= 1
            if follow[1] < lead[1]:
                follow[1] += 1
            else:
                follow[1] -= 1
    return follow

head_loc = [0,0]
visit0 = [] # stores loc visited by tail
visit9 = []

loc9 = [[0,0] for _ in range(9)]

for inst in instructions:
    dir, n = inst.split()
    for _ in range(int(n)):
        if dir == 'U':
            head_loc[1] += 1
        elif dir == 'D':
            head_loc[1] -= 1
        elif dir == 'L':
            head_loc[0] -= 1
        elif dir == 'R':
            head_loc[0] += 1

        loc9[0] = update_follow(loc9[0], head_loc)
        for i in range(1, len(loc9)):
            loc9[i] = update_follow(loc9[i], loc9[i-1])

        if loc9[0] not in visit0:
            visit0.append(loc9[0].copy())
            
        if loc9[-1] not in visit9:
            visit9.append(loc9[-1].copy())

print("Part 1", len(visit0))
print("Part 2", len(visit9))