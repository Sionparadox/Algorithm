import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

L, C = map(int, input().split())
letters = list(input().strip().split(' '))
letters.sort()

vowels = set(['a','e','i','o','u'])
def validation(word):
    cnt = 0
    for i in range(L):
        if word[i] in vowels:
            cnt += 1
    
    return 1<=cnt<=L-2
    
def backTrack(idx, word):
    
    if len(word) == L and validation(word):
        print(word)
    
    for i in range(idx, C):
        backTrack(i+1, word+letters[i])

backTrack(0, '')

'''
i) 모음의 범위를 제한해서 제한된 범위의 모음 + 자음으로 정답 계산
ii) 가능한 모든 경우를 구한 후 각각에 대해 검증
ii부터 시도

'''