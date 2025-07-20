import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

relation = [[0]*N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    relation[u-1][v-1] = 1
    relation[v-1][u-1] = -1

for k in range(N):
    for i in range(N-1):
        for j in range(i+1, N):
            if relation[i][k] == 1 and relation[k][j] == 1:
                relation[i][j] = 1
                relation[j][i] = -1
            elif relation[i][k] == -1 and relation[k][j] == -1:
                relation[i][j] = -1
                relation[j][i] = 1

for rel in relation:
    print(rel.count(0)-1)