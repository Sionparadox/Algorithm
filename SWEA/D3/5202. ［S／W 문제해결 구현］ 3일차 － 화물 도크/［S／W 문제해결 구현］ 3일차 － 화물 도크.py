T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key= lambda x: (x[1],x[0]))
    time = 0
    answer = 0
    for s, e in arr:
        if time <= s:
            time = e
            answer += 1
    print(f'#{t} {answer}')