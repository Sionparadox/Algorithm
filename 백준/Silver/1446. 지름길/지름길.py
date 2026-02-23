import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcuts = {}
for _ in range(N):
    s, e, d = map(int, input().split())
    if e<=D and e-s>d:
        if s not in shortcuts:
            shortcuts[s] = []
        shortcuts[s].append((e, d))

dist = [x for x in range(D+1)]

for s in range(D):
    if s in shortcuts:
        for e, d in shortcuts[s]:
            dist[e] = min(dist[e], dist[s]+d)
    
    dist[s+1] = min(dist[s+1], dist[s]+1)
            
print(dist[D])


'''
dist 배열을 만들고 dist에 대해 반복문
해당 위치에서 시작하는 지름길이 있으면 끝나는 위치 업데이트
+다음 위치를 업데이트
'''