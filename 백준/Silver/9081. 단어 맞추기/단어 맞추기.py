import sys
input = sys.stdin.readline

T = int(input())
words = [list(input().strip()) for _ in range(T)]

for word in words:
    idx = -1
    for i in range(len(word)-2, -1, -1):
        if word[i] < word[i+1]:
            idx = i
            break
    if idx == -1:
        print(''.join(word))
        continue

    for j in range(len(word)-1, idx, -1):
        if word[j] > word[idx]:
              break
    
    word[idx], word[j] = word[j], word[idx]
    word[idx+1:] = word[idx+1:][::-1]
    print(''.join(word))

'''
뒤에서부터 앞으로 오며 앞에 있는 값이 작은지 확인
작은 값이 있다면 해당 위치를 기억. 이후 다시 뒤로가며 이 값보다 바로 다음 큰 수를 찾음.
둘 위치를 바꾸고 기억한 위치 뒤를 뒤집어버리기
'''
