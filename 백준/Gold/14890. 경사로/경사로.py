import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

    
def slope(arr):
    placed = set()
    for i in range(N-1):
        if arr[i+1] == arr[i]:
            continue
        if abs(arr[i+1] - arr[i]) > 1:
            return False
        if arr[i+1] > arr[i]:
            if i<L-1 or i in placed:
                return False
            else:
                placed.add(i)
                for k in range(1, L):
                    if arr[i] != arr[i-k] or i-k in placed:
                        return False
                    placed.add(i-k)
        else:
            if i>=N-L:
                return False
            else:
                placed.add(i+1)
                for k in range(1, L):
                    if arr[i+1] != arr[i+k+1]:
                        return False
                    placed.add(i+k+1)

    return True

answer = 0
for line in board:
    if slope(line):
        answer += 1
    
for line in zip(*board):
    if slope(line):
        answer += 1

print(answer)