import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]
word = input().strip()
L = len(word)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[[-1]*L for _ in range(M)] for _ in range(N)]

def DFS(r, c, idx):
    if idx == L-1:
        return 1
    if dp[r][c][idx] != -1:
        return dp[r][c][idx]
    
    res = 0
    nxt = word[idx+1]
    for dr, dc in directions:
        for k in range(1, K+1):
            nr, nc = r+dr*k, c+dc*k
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if board[nr][nc] == nxt:
                res += DFS(nr, nc, idx+1)
    dp[r][c][idx] = res
    return res

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == word[0]:
            answer += DFS(i, j, 0)
print(answer)


'''
DFS로 다음 문자로 넘어가며 경로 수를 세려함.
>> 시간초과 우려
중복되는 경로 탐색을 없애야함.
dp[r][c][idx] : r,c 칸에 idx번 문자를 탐색하기 위해 왔을 때 이후 경로의 수
'''