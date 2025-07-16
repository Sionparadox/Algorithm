import sys
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    x, y = map(int ,input().split())
    points.append((x, y))

def distance(i, j):
    return abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])

tot = distance(0, 1)
maxDiff = 0
for i in range(1, N-1):
    tot += distance(i, i+1)
    maxDiff = max(maxDiff, distance(i-1, i) + distance(i, i+1) - distance(i-1, i+1))

print(tot-maxDiff)