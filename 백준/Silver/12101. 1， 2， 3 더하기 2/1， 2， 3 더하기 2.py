import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
def backTrack(n, arr):
    global cnt
    if n == 0:
        cnt += 1
        if cnt == K:
            print('+'.join(map(str, arr)))
            exit()
        return
    
    backTrack(n-1, arr+[1])
    if n>=2:
        backTrack(n-2, arr+[2])
    if n>=3:
        backTrack(n-3, arr+[3])

backTrack(N, [])
print(-1)  
            