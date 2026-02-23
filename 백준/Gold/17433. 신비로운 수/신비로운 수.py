import sys
input = sys.stdin.readline

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x%y)

T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    diff = []
    for i in range(1,N):
        diff.append(arr[i]-arr[0])
    if all(d == 0 for d in diff):
        print("INFINITY")
        continue
    
    answer = diff[0]
    for d in diff[1:]:
        answer = GCD(answer, d)
    print(abs(answer))

'''
모든 수가 같을 때에만 발산
각 수를 바꿨을 떄
ak+m, bk+m, ck+m 같은 형식이 되면 1이 아닌 M이 존재
-> bk-ak = xk
-> ck-ak = yk
각 수의 차이가 가지는 최대공약수가 답
x%y = r
GCD(x, y) = GCD(y, r)

'''