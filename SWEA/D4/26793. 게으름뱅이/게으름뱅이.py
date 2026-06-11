T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        d, t = map(int, input().split())
        arr.append((d, t))
    arr.sort(key=lambda x: x[1], reverse=True)
 
    answer = arr[0][1]
    for d, t in arr:
        if t < answer:
            answer = t
        answer -= d
    print(answer)