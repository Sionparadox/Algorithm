import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

wordIdx = {}
maxLen = 0
answer = ['','']
for i in range(N):
    word = words[i]
    
    for l in range(1, len(word)+1):
        part = word[:l]
        if part in wordIdx:
            if words[wordIdx[part]] != word:
                
                if maxLen == l and answer[0] > wordIdx[part]:
                    answer = [wordIdx[part], i]
                    
                elif maxLen<l:
                    maxLen = l
                    answer = [wordIdx[part], i]
        else:
            wordIdx[part] = i

print(words[answer[0]]) 
print(words[answer[1]])
'''
wordIdx : 모든 접두사의 위치를 저장하는 딕셔너리
'noon'에 대해 'n', 'no', 'noo', 'noon' 다 인덱스를 저장해두기
'''