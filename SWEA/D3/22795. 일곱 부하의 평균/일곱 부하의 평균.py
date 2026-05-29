T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    ans = max(arr)+1
    remains = (ans+sum(arr))%7
    print(ans + 7-remains if remains != 0 else ans)
