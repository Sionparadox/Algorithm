import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

answer = 0

def find_quarter(r, c, depth):
    global answer
    
    half = (1<<(N-depth))
    res = 0
    if r >= half:
        res += 2
        r -= half
    if c >= half:
        res += 1
        c -= half
    
    answer += (half**2)*res
    return r, c

for d in range(1,N+1):
    r, c = find_quarter(r, c, d)

print(answer)


'''
depth에 따라 R,C를 좌상단으로 오도록 좌표변경 시키며 answer에 누적시키기

'''