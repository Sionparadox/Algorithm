from collections import deque
def solution(begin, target, words):
    L = len(words)
    visited = [False]*L
    queue = deque()
    queue.append((begin, 0))
    while queue:
        curr, k = queue.popleft()
        for i in range(L):
            if not visited[i] and canChange(curr, words[i]):
                if words[i] == target: return k+1
                visited[i] = True
                queue.append((words[i], k+1))
    return 0


def canChange(w1, w2):
    res = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]: res += 1
    return res == 1