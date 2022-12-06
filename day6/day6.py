#--- Day 6: Tuning Trouble ---
# start of packet: 4 different characters
import sys
ls = []
with open(sys.argv[1], 'r') as f:
    ls = f.read().split('\n')

signal = ls[0]
def check_distinct(n:int, s:str):
    """
        check at which index the given string of length n only contains distinct characters
    """
    i = 0
    while i+n < len(s):
        ch = []
        dupe = False
        for j in s[i:i+n]:
            if j not in ch:
                ch.append(j)
            else:
                dupe = True
                break
        # print(ch)
        if dupe == False:
            print(ch, i+n)
            break
        i+=1

check_distinct(4, signal)
check_distinct(14, signal)