import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
watched = [[False]*M for _ in range(N)]
cctv = []
indicator = {'r':[0, 1], 'l':[0, -1], 'u':[-1, 0], 'd':[1, 0]}
directions = [[''],['r','d','l','u'],['lr','ud'],['rd','dl','lu','ur'],['rdl','dlu','lur','urd'],['lrud']]

def fill(arr, pos, d):
    res = [row[:] for row in arr]
    r = pos//M
    c = pos%M
    res[r][c] = True
    
    for s in d:
        dr, dc = indicator[s]
        nr, nc = r, c
        while True:
            nr, nc = nr+dr, nc+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                break
            if room[nr][nc] == 6:
                break
            res[nr][nc] = True
    
    return res

for r in range(N):
    for c in range(M):
        if room[r][c] == 0:
            continue
        
        if room[r][c] == 5:
            watched = fill(watched, r*M+c, directions[5][0])
        
        elif room[r][c] != 6:
            cctv.append(r*M+c)
        else:
            watched[r][c] = True

answer = float('inf')  
def DFS(idx, arr):
    global answer
    if idx == len(cctv):
        res = sum([line.count(False) for line in arr])
        answer = min(answer, res)
        return
    
    r = cctv[idx]//M
    c = cctv[idx]%M
    num = room[r][c]
    for dir in directions[num]:
        new_arr = fill(arr, cctv[idx], dir)
        DFS(idx+1, new_arr)
DFS(0, watched)
print(answer)