import sys
input = sys.stdin.readline

N, M = map(int, input().split())

heavy = [[False]*N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    heavy[u-1][v-1] = True

for k in range(N):
    for i in range(N):
        for j in range(N):
            if heavy[i][k] and heavy[k][j]:
                heavy[i][j] = True

answer = 0
for i in range(N):
    h = 0
    l = 0
    for j in range(N):
        if heavy[i][j]:
            h += 1
        if heavy[j][i]:
            l += 1
    if h >= (N+1)//2 or l >= (N+1)//2:
        answer += 1

print(answer)

'''
heavy[a][b] : a가 b보다 무거움
플로이드 워셜로 관계 설정 N^2 최대 1,000,000
한 구슬보다 무거운 or 가벼운 구슬이 절반 이상이면 불가능
'''