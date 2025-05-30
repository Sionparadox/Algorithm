import sys
input = sys.stdin.readline

def isPalindrome(s):
    L = len(s)
    for i in range(L//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

s = input().strip()
answer = len(s)
if isPalindrome(s):
    key = s[0]
    for c in s:
        if key != c:
            print(answer-1)
            exit()
    print(-1)
else:
    print(answer)
    