import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def findTeam(k, path, pathSet):
    visited[k] = True
    path.append(k)
    pathSet.add(k)
    next = students[k]
    if not visited[next]:
        return findTeam(next, path, pathSet)
    elif next in path:
        idx = path.index(next)
        return path[idx:]
    return []

T = int(input())
for _ in range(T):
    N = int(input())
    students = [x-1 for x in list(map(int, input().split()))]
    team = [False]*N
    visited = [False]*N
    for i in range(N):
        if not visited[i]:
            cycle = findTeam(i,[], set())
            for c in cycle:
                team[c] = True
    print(team.count(False))
    