T = int(input())
for t in range(1, T+1):
    nums = list(map(int, list(input().strip())))
    k = len(nums)-1 + (sum(nums)-1)//9
    answer = 'A' if k%2 else 'B'
    print(f'#{t} {answer}')