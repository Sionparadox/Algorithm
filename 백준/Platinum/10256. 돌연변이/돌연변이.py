import sys
from collections import deque
input = sys.stdin.readline

mapper = {'A':0, 'C':1, 'G':2, 'T':3}
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dna = input().strip()
    marker = input().strip()
    
    mutated = set()
    for i in range(M):
        for j in range(i, M):
            mutated.add(marker[:i] + marker[i:j+1][::-1] + marker[j+1:])
        
    children =[[-1, -1, -1, -1]]
    is_finish = [False]
    
    for mark in mutated:
        curr = 0
        for ch in mark:
            idx = mapper[ch]
            if children[curr][idx] == -1:
                children[curr][idx] = len(children)
                children.append([-1, -1, -1, -1])
                is_finish.append(False)
                
            curr = children[curr][idx]
        is_finish[curr] = True
    
    fail = [0]*len(children)
    queue = deque([0])
    
    while queue:
        curr = queue.popleft()
        
        for i in range(4):
            nxt = children[curr][i]
            if nxt != -1:
                if curr == 0:
                    fail[nxt] = 0
                else:
                    fail[nxt] = children[fail[curr]][i]
                
                if is_finish[fail[nxt]]:
                    is_finish[nxt] = True
                
                queue.append(nxt)
            
            else:
                if curr == 0:
                    children[curr][i] = 0
                else:
                    children[curr][i] = children[fail[curr]][i]
    
    
    curr = 0
    res = 0
    for ch in dna:
        idx = mapper[ch]
        curr = children[curr][idx]
        if is_finish[curr]:
            res += 1
    
    print(res)
'''
기존처럼 딕셔너리로 구현 시 시간초과남.
children[node][ch] : 다음 노드 인덱스 이런식으로 구현

'''
        