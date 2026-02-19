import sys
import itertools
input = sys.stdin.readline

atoi = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11}

N, M = map(int, input().split())

notes = list(map(lambda x:atoi.get(x), input().split()))
codes = list(map(lambda x:atoi.get(x), input().split()))

difficulty = float('inf')

for target in itertools.product(range(M), repeat=N):
    if len(set(target)) != M:
        continue
    fret = []
    for line in range(N):
        diff = (codes[target[line]] - notes[line])%12
        if diff != 0:
            fret.append(diff)
    
    if len(fret) == 0:
        difficulty = 0
        break
    
    gap = 0
    fret.sort()
    for i in range(len(fret)-1):
        gap = max(gap, fret[i+1] - fret[i])
    gap = max(gap, fret[0]-fret[-1]+12)
    
    difficulty = min(difficulty, 12-gap+1)

print(difficulty)
'''
각 음 차이를 구할 때 12높은 프렛을 눌러도 음이 같음
-> 프렛 하나를 12높일 경우 최대, 최소 프렛이 바뀜
프렛을 정렬 후 각 인접 프렛끼리 차이를 구함. 그리고 12에서 그 차이를 뻄.
=> 차이가 가장 큰 쌍에서 큰 값이 최소값이 되고 작은값 이하 수들은 다 12가 더해진다고 생각하면 됨 
'''      
