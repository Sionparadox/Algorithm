import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
seq = input().rstrip().replace(' ','')
target = ''.join([str(x) for x in range(1, N+1)])

queue = deque([(seq, 0)])
visited = set([seq])

answer = -1
while queue:
    nums, cnt = queue.popleft()
    if nums == target:
        answer = cnt
        break
    for i in range(N-K+1):
        new_nums = nums[:i]+nums[i:i+K][::-1]+nums[i+K:]
        if new_nums not in visited:
            queue.append((new_nums, cnt+1))
            visited.add(new_nums)

print(answer)

'''
BFS로 돌리기?
'''