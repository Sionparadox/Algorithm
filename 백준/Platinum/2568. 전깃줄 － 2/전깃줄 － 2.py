import sys
import bisect
input = sys.stdin.readline

N = int(input())
line = {}
btoa = {}
end = 0
for _ in range(N):
    a, b = map(int, input().split())
    line[a] = b
    btoa[b] = a
    end = max(end, a, b)

nums = []
for i in range(end+1):
    if i in line:
        nums.append(line[i])

dp = []
pos = [0]*N
for i in range(N):
    idx = bisect.bisect_left(dp, nums[i])
    if idx == len(dp):
        dp.append(nums[i])
    else:
        dp[idx] = nums[i]
    pos[i] = idx

k = len(dp)-1
left = set()
cut = []
for i in range(N-1, -1, -1):
    if pos[i] == k:
        k -= 1
        left.add(i)
    else :
        cut.append(btoa[nums[i]])

print(N-len(dp))
print('\n'.join(map(str, sorted(cut))))



'''
1~N에 대응하는 반대 위치를 배열로 저장
오름차순을 만드는 부분수열의 길이중 가장 긴것이 정답 (lis)
dp에 길이를 저장하며 탐색하니 시간초과(N^2)
이분탐색으로 방식을 변경. dp에 LIS를 만드는 최소크기 노드를 저장하며 가는것. << 같은 길이라면 값이 작은 노드가 이후 추가적으로 만드는데 유리함.

'''