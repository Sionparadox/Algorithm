import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
S = []
cnt = 0
for n in arr:
    if n % 2 == 1:
        if cnt != 0: 
            S.append(cnt)
        cnt = 0
        S.append(cnt)
    else:
        cnt += 1
if cnt != 0 :
    S.append(cnt)

left = right = 0
odd = total = 0
answer = 0

while right<len(S):
    if S[right] == 0:
        odd += 1
    else :
        total += S[right]
    
    while odd > K:
        if S[left] == 0:
            odd -= 1
        else :
            total -= S[left]
        left += 1
    
    answer = max(answer, total)
    right += 1

print(answer)
