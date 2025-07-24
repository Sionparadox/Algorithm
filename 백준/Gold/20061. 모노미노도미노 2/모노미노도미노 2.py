import sys
input = sys.stdin.readline

def findTop(arr, c):
    for r in range(1,6):
        if arr[r][c] == 1:
            return r-1
    return 5

def filled(arr, row):
    if row >5: return False
    if sum(arr[row]) == 4:
        arr.pop(row)
        arr.insert(0, [0]*4)
        return True
    return False

def remove(arr):
    cnt = 0
    for r in (0,1):
        for c in range(4):
            if arr[r][c] == 1:
                cnt += 1
                break
    
    for i in range(cnt):
        arr.pop(5)
        arr.insert(0, [0]*4)

def fall(arr, c1, c2, shape):
    global answer
    height = min(findTop(arr, c1), findTop(arr, c2))
    arr[height][c1] = 1
    if shape == 'v':
        height -= 1
    arr[height][c2] = 1

    if filled(arr, height):
        answer += 1
    if filled(arr, height+1):
        answer += 1
    
    remove(arr)

N = int(input())   
G = [[0]*4 for _ in range(6)]
B = [[0]*4 for _ in range(6)]   
answer = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        fall(G, y, y, 'o')  
        fall(B, 3-x, 3-x, 'o')  
    elif t == 2:
        fall(G, y, y+1,'h')
        fall(B, 3-x, 3-x, 'v')
    else:
        fall(G, y, y, 'v')
        fall(B, 2-x, 3-x, 'h')

print(answer)        
print(sum(sum(row) for row in G) + sum(sum(row) for row in B))