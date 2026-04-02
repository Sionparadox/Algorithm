import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    cmd = input().split()
    if len(cmd) == 2:
        x = int(cmd[1])
    
    if cmd[0] == 'add':
        S.add(x)
    elif cmd[0] == 'remove':
        S.discard(x)
    elif cmd[0] == 'check':
        print(1 if x in S else 0)
    elif cmd[0] == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cmd[0] == 'all':
        S = set(range(1, 21))
    elif cmd[0] == 'empty':
        S.clear()
