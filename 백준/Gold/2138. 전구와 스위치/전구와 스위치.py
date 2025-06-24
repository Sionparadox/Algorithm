import sys
input = sys.stdin.readline

N = int(input())
start = list(map(int, input().strip()))
end = list(map(int, input().strip()))
start2 = start[:]

def turn(s, idx):
    L = max(idx-1, 0)
    R = min(idx+1, N-1)
    for i in range(L, R+1):
          s[i] = 1-s[i]

turn(start2, 0)
cnt = [0, 1]
for i in range(0, N-1):
    if start[i] != end[i]:
        turn(start, i+1)
        cnt[0] += 1
    if start2[i] != end[i]:
        turn(start2, i+1)
        cnt[1] += 1

answer = float('inf')
if start[N-1] == end[N-1]:
    answer = min(answer, cnt[0])
if start2[N-1] == end[N-1]:
    answer = min(answer, cnt[1])

print(answer if answer != float('inf') else -1)