from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    A = deque(map(int, input().split()))
    B = deque(map(int, input().split()))
    answer = ['']*(N+1)
    cnt = 0
    for i in range(N):
        if i%2 == 0:
            while A:
                player = A.popleft()
                if answer[player] == '':
                    answer[player] = 'A'
                    break
                
        else:
            while B:
                player = B.popleft()
                if answer[player] == '':
                    answer[player] = 'B'
                    break
    
    print(''.join(answer))
