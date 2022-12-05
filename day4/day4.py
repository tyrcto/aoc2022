#--- Day 4: Camp Cleanup ---
import sys

with open(sys.argv[1], 'r') as f:
    sections = f.read().split('\n')

fully = 0
for pair in sections:
    p0,p1 = pair.split(',')
    p0 = list(map(int, p0.split('-')))
    p1 = list(map(int, p1.split('-')))

    s0 = set(list(range(p0[0], p0[1]+1)))
    s1 = set(list(range(p1[0], p1[1]+1)))

    if len(s0) == 0:
        s0 = set([p0[0]])
    if len(s1) == 0:
        s1 = set([p1[0]])
    if s0.issubset(s1) or s1.issubset(s0):
        fully += 1

print("Part 1", fully)

at_all = 0
for pair in sections:
    p0,p1 = pair.split(',')
    p0 = list(map(int, p0.split('-')))
    p1 = list(map(int, p1.split('-')))

    s0 = set(list(range(p0[0], p0[1]+1)))
    s1 = set(list(range(p1[0], p1[1]+1)))

    if len(s0) == 0:
        s0 = set([p0[0]])
    if len(s1) == 0:
        s1 = set([p1[0]])
    if len(s0.intersection(s1)):
        at_all += 1

print("Part 2", at_all)