from collections import deque

def remove(n):
    queue.append(n)
    while queue:
        idx = queue.popleft()
        coins[idx] = -1
        if idx > 0 and coins[idx-1] != -1:
            coins[idx-1] = 1-coins[idx-1]
            if coins[idx-1]:
                queue.append(idx-1)
        if idx < N-1 and coins[idx+1] != -1:
            coins[idx+1] = 1-coins[idx+1]
            if coins[idx+1]:
                queue.append(idx+1)
    
    

TC = int(input())
for tc in range(1, TC+1):
    coins = list(map(int, list(input())))
    N = len(coins)
    queue = deque()
    for i in range(N):
        if coins[i] == 1:
            remove(i)
    print(f"#{tc} {'yes' if all(x for x in coins) else 'no'}")