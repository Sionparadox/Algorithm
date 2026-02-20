import sys
input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    words.append(input().rstrip())

words.sort()

answer = N
for i in range(N-1):
    if len(words[i]) <= len(words[i+1]) and words[i] == words[i+1][:len(words[i])]:
        answer -= 1
    
print(answer)