import sys
input = sys.stdin.readline

def make_pi(word):
    W = len(word)
    pi = [0]*W
    
    j = 0
    for i in range(1, W):
        while j>0 and word[i] != word[j]:
            j = pi[j-1]
        
        if word[i] == word[j]:
            j += 1
            pi[i] = j
        
    return pi

def solve(word):
    W = len(word)
    pi = make_pi(word)
    
    p = W-pi[-1]
    if W%p == 0:
        return W//p
    else:
        return 1

while True:
    _input = input().strip()
    if _input == '.': break
    ans = solve(_input)
    print(ans)
    
'''
KMP 풀듯 pi배열을 만들어서 반복 주기를 찾아냄.
주기가 전체 길이와 안맞으면 제곱으로 못만드는 것
'''