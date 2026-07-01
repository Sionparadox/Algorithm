TC = int(input())
answer = []
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(M-1):
        seq = list(map(int, input().split()))
        k = seq[0]
        
        pos = len(nums)
        for i in range(len(nums)):
            if nums[i] > k:
                pos = i
                break
        
        nums[pos:pos] = seq
    print(f'#{tc}', *nums[-10:][::-1])