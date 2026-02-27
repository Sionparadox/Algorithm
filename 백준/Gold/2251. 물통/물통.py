import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A, B, C = map(int, input().split())
visited = [[[False]*(C+1) for _ in range(B+1)] for _ in range(A+1)]

answer = []
def DFS(a,b,c):
    if visited[a][b][c]:
        return
    if a == 0:
        answer.append(c)
    
    visited[a][b][c] = True
    a_left = A-a
    b_left = B-b
    c_left = C-c
    if a_left:
        DFS(min(A, a+b), max(0,b-a_left), c)
        DFS(min(A, a+c), b, max(0, c-a_left))
    if b_left:
        DFS(max(0, a-b_left), min(B, a+b) , c)
        DFS(a, min(B, b+c), max(0, c-b_left))
    if c_left:
        DFS(max(0, a-c_left), b, min(C, a+c))
        DFS(a, max(0, b-c_left), min(C, b+c))

DFS(0,0,C)
print(*sorted(answer))

'''
방문체크하며 DFS로 값 갱신
b->a, c->a
a->b, c->b
a->c, b->c

'''