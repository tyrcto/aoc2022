# --- Day 8: Treetop Tree House ---
# how many trees are visible from outside the grid?
import sys

map = []
with open(sys.argv[1], 'r') as f:
    map=f.read().splitlines()

count = 0
maxh = len(map)
maxw = len(map[0])
for i in range(1,maxh-1):
    for j in range(1, maxw-1):
        # check current tree at(i,j) visibility
        up, down, left, right = [True]*4

        for a in range(0,i):
            if map[a][j]>=map[i][j]:
                up=False
                break
        for a in range(i+1,maxh):
            if map[a][j]>=map[i][j]:
                down=False
                break
        for a in range(0,j):
            if map[i][a]>=map[i][j]:
                left=False
                break
        for a in range(j+1,maxw):
            if map[i][a]>=map[i][j]:
                right=False
                break
        if up or down or left or right:
            count+=1

edge_trees = (maxw-1)*2 + (maxh-1)*2 
print("Part 1", count+edge_trees)

max_scenic_score = -1
for i in range(1,maxh-1):
    for j in range(1, maxw-1):
        c_up, c_down, c_left, c_right = [0]*4

        # range is reversed so that checks start from current tree, outwards, towards the edges
        for a in reversed(range(0,i)):
            c_up+=1
            if map[a][j]>=map[i][j]:
                break
        for a in (range(i+1,maxh)):
            c_down+=1
            if map[a][j]>=map[i][j]:
                break
        for a in reversed(range(0,j)):
            c_left+=1
            if map[i][a]>=map[i][j]:
                break
        for a in (range(j+1,maxw)):
            c_right+=1
            if map[i][a]>=map[i][j]:
                break
        
        # print(f"{map[i][j]}: {c_up, c_down, c_left, c_right}")
        scenic_score = c_up*c_down*c_left*c_right
        if max_scenic_score< scenic_score:
            max_scenic_score = scenic_score

print("Part 2", max_scenic_score)
