import sys
input = sys.stdin.readline

N, K = map(int, input().split())
fishes = list(map(int, input().split()))

def fillMin():
    minVal = min(fishes)
    for i in range(N):
        if fishes[i] == minVal:
            fishes[i] += 1

def adjust(arr):
    temp = []
    for ar in arr:
        if ar:
            temp.append(ar)
    L = len(temp)
    H = len(temp[0])
    res = [[0]*H for _ in range(L)]
    for i in range(L):
        for j in range(len(temp[i])):
            if i<L-1 and j<len(temp[i+1]):
                d = abs(temp[i][j] - temp[i+1][j])//5
                if temp[i][j] > temp[i+1][j]:
                    d *= -1
                res[i][j] += d
                res[i+1][j] -= d
            
            if j<len(temp[i])-1:
                d = abs(temp[i][j] - temp[i][j+1])//5
                if temp[i][j] > temp[i][j+1]:
                    d *= -1
                res[i][j] += d
                res[i][j+1] -= d
    for i in range(L):
        for j in range(len(temp[i])):
            temp[i][j] += res[i][j]
    return temp

def flat(arr):
    res = []
    for ar in arr:
        res.extend(ar)
    return res

def levitate():
    res = [[] for _ in range(N)]
    for i in range(N):
        res[i].append(fishes[i])
    
    res[1].append(res[0].pop())
    sidx = 1
    while True:
        cnt = 0
        for eidx in range(sidx, N):
            if len(res[eidx])<2:
                break
            cnt += 1
        H = len(res[sidx])
        if H > (N-cnt-sidx):
            break
        
        for i in range(cnt):
            idx = sidx+(cnt-i-1)
            for k in range(H):
                res[eidx+k].append(res[idx][k])
            res[idx] = []
        sidx = eidx
    res = adjust(res)
    res = flat(res)
    return res

def half():
    res = [[0]*(4) for _ in range(N//4)]
    for i in range(4):
        arr = fishes[i*(N//4):(i+1)*(N//4)]
        if i%2==0:
            arr = arr[::-1]
        for j in range(N//4):
            res[j][(i+1) % 4] = arr[j]
    
    res = adjust(res)
    res = flat(res)
    return res


answer = 0
while True:
    answer += 1
    fillMin()
    fishes = levitate()
    fishes = half()
    if max(fishes) - min(fishes) <= K:
        break

print(answer)

'''
1 2 3 4 5 6 7 8

4 3 2 1
5 6 7 8

6 5
3 4
2 1
7 8

1 2 3 4 5 6 7 8 9 T J Q

6 5 4 3 2 1
7 8 9 T J Q

9 8 7   (2/4 영역) 반
4 5 6   (1/4 영역) 정
3 2 1   (0/4 영역) 반
T J Q   (3/4 영역) 정 
3 -> 0
0 -> 1
1 -> 2
2 -> 3
'''