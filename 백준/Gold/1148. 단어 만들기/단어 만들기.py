import sys
import itertools
input = sys.stdin.readline

words = set()
while True:
    _input = input().rstrip()
    if _input == '-':
        break
    words.add(_input)

while True:
    _input = input().rstrip()
    if _input == '#':
        break
    
    cnt = {}
    for c in set(list(_input)):
        cnt[c] = 0

    canmake = set()
    for length in range(4, 10):
        for letters in itertools.permutations(_input, length):
            word = ''.join(letters)
            if word in words:
                canmake.add(word)
    
    for word in canmake:
        for c in set(list(word)):
            if c in cnt:
                cnt[c] += 1
    
    min_value = min(cnt.values())
    max_value = max(cnt.values())
    max_letter = ''.join(sorted([key for key, value in cnt.items() if value == max_value]))
    min_letter = ''.join(sorted([key for key, value in cnt.items() if value == min_value]))
    print(min_letter, min_value, max_letter, max_value)



'''
1. 각 case에 대해 20만번 단어를 순회
    => C*200,000* 9이하(단어를 만들 수 있는지 파악)
2. 각 case에 대해 만들 수 있는 단어를 미리 만들어두고 단어 집합에서 찾기
    9! = 약 36만
    => C*80만 이상
'''
