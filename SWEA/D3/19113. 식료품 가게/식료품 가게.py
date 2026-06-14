from collections import defaultdict
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = []
    cnt = defaultdict(int)
    for p in arr:
        if cnt[p]>0:
            cnt[p] -= 1
        else:
            cnt[p*4//3] += 1
            answer.append(p)
    print(f'#{tc}',*answer)