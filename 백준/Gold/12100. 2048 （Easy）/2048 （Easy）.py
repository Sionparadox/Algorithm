import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate(arr, k=1):
    copied = arr
    for _ in range(k):
        copied = [list(reversed(col)) for col in zip(*copied)]
    return copied

def moveleft(arr):
    res = []
    for row in arr:
        temp = [0]*N
        idx = 0
        for n in row:
            if n == 0:
                continue
            if temp[idx] == n:
                temp[idx] += n
                idx += 1
            elif temp[idx] == 0:
                temp[idx] = n
            else :
                idx += 1
                temp[idx] = n
        res.append(temp)
    return res

answer = 0
def play(arr, k):
    global answer
    if k == 5:
        val = max(max(row) for row in arr)
        answer = max(answer, val)
        return
    
    for i in range(4):
        rotated = rotate(arr, i)
        moved = moveleft(rotated)
        play(moved, k+1)
play(board, 0)
print(answer)                
