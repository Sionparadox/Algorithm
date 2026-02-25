import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())

if K<5:
    print(0)
    exit(0)
if K == 26:
    print(N)
    exit(0)

def word_to_mask(word):
    res = 0
    for c in word:
        res |= (1 << (ord(c) - ord('a')))
    
    return res

arr = []
presuf = word_to_mask('antic')

for _ in range(N):
    _input = input().rstrip()
    arr.append(word_to_mask(_input))

K -= 5
answer = 0

def backTrack(idx, mask, length):
    global answer
    
    if length == K:
        cnt = 0
        for word in arr:
            if (word & mask) == word:
                cnt += 1
        answer = max(answer, cnt)
    
    for i in range(idx, 26):
        if mask & (1<<i):
            continue
        backTrack(i+1, mask | (1<<i), length+1)
    
backTrack(0, presuf, 0)
print(answer)

'''
anta,tica -> {a,n,t,i,c}
집합으로 체크하며 백트래킹 -> 시간초과
집합을 사용하지 않고 비트마스킹으로 방문처리

'''