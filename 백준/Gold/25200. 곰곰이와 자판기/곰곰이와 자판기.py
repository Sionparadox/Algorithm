import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(M):
    arr.append(tuple(map(int, input().split())))

answer = list(range(N+1))
for u, v in reversed(arr):
    answer[u] = answer[v]

print(*answer[1:])


'''
union-find?
-> No,이전 부모 갱신은 다음 입력에 적용되면 안됨
이전 이동이 다음 이동이후에 영향을 줘서는 안됨.
뒤집어서 처리
'''