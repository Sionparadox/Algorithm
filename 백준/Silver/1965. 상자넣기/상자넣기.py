import sys
import bisect
input = sys.stdin.readline

N = int(input())
boxes = list(map(int, input().split()))

seq = [boxes[0]]

for size in boxes[1:]:
    idx = bisect.bisect_left(seq, size)
    if idx==len(seq):
        seq.append(size)
    else:
        seq[idx] = size
    
print(len(seq))

'''
LIS
'''