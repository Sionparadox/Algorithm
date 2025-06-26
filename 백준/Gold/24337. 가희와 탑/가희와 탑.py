import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

if b>a:
    front = [x for x in range(1, a)]
    back = [x for x in range(b, 0, -1)]
else:
    front = [x for x in range(1, a+1)]
    back = [x for x in range(b-1, 0, -1)]
answer = front+back

if len(answer) > N:
    print(-1)
elif a == 1:
    answer = [answer[0]] + [1]*(N-len(answer)) + answer[1:]
    print(' '.join(map(str, answer)))
else:
    answer = [1]*(N-len(answer)) + answer
    print(' '.join(map(str, answer)))
'''
뒤에서부터 1~b 역순
앞에서부터 1~a
둘중 큰거 먼저 채우기.
이후 남는 길이만큼 앞에 1 패딩
'''