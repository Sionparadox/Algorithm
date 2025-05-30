import sys
input = sys.stdin.readline

N = int(input())
road = 'E'+input().strip()
visited = [-1]*N

answer = 0
for i in range(N):
    if road[i] == 'E' and road[i+1] == 'W':
        answer += 1
print(answer)