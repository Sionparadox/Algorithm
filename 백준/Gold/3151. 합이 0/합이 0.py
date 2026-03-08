import sys
input = sys.stdin.readline

N = int(input())
if N < 3:
    print(0)
    exit()

arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(N - 2):
    target = -arr[i]
    left = i + 1
    right = N - 1
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            if arr[left] == arr[right]:
                answer += right - left
                left += 1
            else:
                l_idx, r_idx = left, right
                while l_idx < right and arr[l_idx] == arr[left]:
                    l_idx += 1
                while r_idx > left and arr[r_idx] == arr[right]:
                    r_idx -= 1
                answer += (right-r_idx)*(l_idx-left)
                left, right = l_idx, r_idx
                
print(answer)