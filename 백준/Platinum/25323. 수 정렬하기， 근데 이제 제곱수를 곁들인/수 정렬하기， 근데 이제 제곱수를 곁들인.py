import sys, math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)

flag = True
for i in range(N):
    k = arr[i]*sorted_arr[i]
    if math.isqrt(k) ** 2 != k:
        flag = False
        break

print("YES" if flag else "NO")

'''
정렬된 배열과 원래 배열을 곱해 제곱수가 나오는지 판단
m*k^2 모양에서 m이 같으면 원래수를 곱하면 제곱수가 나옴
'''