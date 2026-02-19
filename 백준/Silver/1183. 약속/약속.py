import sys
input = sys.stdin.readline

N = int(input())
diff = []

for _ in range(N):
    A, B = map(int, input().split())
    diff.append(A-B)
diff.sort()

if N%2 == 1:
    print(1)
else:
    print(diff[N//2]-diff[N//2-1]+1)


'''
항의 개수가 홀수일 때 : 반드시 1가지
diff = A-B
항의 개수가 홀수일 경우 diff를 기준으로 중앙값만이 T가 될 수 있음.
짝수일 경우 중앙값 2개를 포함하는 구간에 포함된 수의 개수

'''