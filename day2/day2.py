# --- Day 2: Rock Paper Scissors ---
# to decide whose tent gets to be closest to snack storage
# 1st col: opp's play [A:Rock; B:Paper; C:Scissors]
# 2nd col: your  play [X:Rock; Y:Paper; Z:Scissors]
# winner w/ highest score
# Scoring:
# Shape -> [1:Rock; 2:Paper; 3:Scissors]
# Outcome -> [0:Lose; 3:Draw; 6:Win]
import sys

fname = sys.argv[1]
lines = []
with open(fname, 'r') as f:
    lines = f.readlines()
total_score1 = 0
for line in lines:
    round_score = 0
    opp, you = line.strip('\n').split(' ')
    o, y = ord(opp)-ord('A'), ord(you)-ord('X') 
    res = y-o
    if res == 1 or res == -2:   # win
        round_score += 6
    elif res == 0:              # draw
        round_score += 3
    round_score += y+1  # add shape score
    total_score1 += round_score

total_score2 = 0
for line in lines:
    round_score = 0
    opp, sign = line.strip('\n').split(' ')
    o, s = ord(opp)-ord('A'), ord(sign)-ord('X') 
    if s == 1:      # must draw
        round_score += 3
        round_score += o+1
    elif s == 2:    # must win
        round_score += 6
        round_score += (o+2) if o<2 else 1
    else:           # must lose
        round_score += (o) if o>0 else 3
    total_score2 += round_score
    # print(round_score)

print(f"Part 1: {total_score1}")
print(f"Part 2: {total_score2}")