import sys
input = sys.stdin.readline

N = input().strip()
cnt = [0]*10
L = len(N)
num = int(N)

for i in range(L):
    power = 10**i
    left = num // (power*10)
    mid = (num // power) % 10
    right = num % power
    for d in range(10):
        cnt[d] += left*power
        if mid > d :
            cnt[d] += power
        elif mid == d:
            cnt[d] += right+1

for i in range(L):
    cnt[0] -= 10**(i)

print(' '.join(map(str, cnt)))
    

'''
3 -> 1~3 1씩 추가
N = 38
8이라는건 8+1 만큼 10의자리가 더 등장했다. + 그 이하 10의 자리는 10번씩 나옴
또한 0~8이 한번씩 나왔음
    3 : +9, 1~2: +10
    0~8 : +1

N = 438
1의자리가 8이기 때문에 3: +9, 0~2 : +10, 0~8: +1
10의자리이후가 38이기 때문에 4: +39, 1~3 : +100

규칙이 있다!
현재 자리수 기준으로 왼쪽, 오른쪽, 중간을 구해서
0~9 수에 대해
기본적으로 left * 10**i만큼 더하고
현재 수(중간)보다 작다면 10**i만큼 더함.
현재수와 같다면 right+1만큼 더함

이후 0이 가장 앞자리에 나오는 경우만큼 빼버리기. 

'''