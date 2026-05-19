T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        cmd = input().split()
        if cmd[0] == 'D':
            del arr[int(cmd[1])]
            continue
        x, y = int(cmd[1]), int(cmd[2])
        if cmd[0] == 'I':
            arr.insert(x, y)
        else:
            arr[x] = y
    
    print(f'#{t} {arr[L] if L<len(arr) else -1}')
        