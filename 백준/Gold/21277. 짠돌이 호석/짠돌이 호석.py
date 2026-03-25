import sys
input = sys.stdin.readline

def rotate(arr):
    return list(map(list, zip(*arr[::-1])))

N, M = map(int, input().split())
P = [input().strip() for _ in range(N)]
P_bits = [int(row, 2) for row in P]

R, C = map(int, input().split())
Q = [list(input().strip()) for _ in range(R)]

answer = float('inf')

curr_Q = Q
for _ in range(4):
    curr_Q = rotate(curr_Q)
    curr_R = len(curr_Q)
    curr_C = len(curr_Q[0])
    
    Q_bits = [int(''.join(row), 2) for row in curr_Q]
    diff = M - curr_C
    
    for dr in range(-curr_R + 1, N):
        for dc in range(-curr_C + 1, M):
            overlapped = False
            move = diff - dc
            
            for r in range(curr_R):
                nr = r + dr
                if 0 <= nr < N:
                    if move >= 0:
                        new_Q = Q_bits[r] << move
                    else:
                        new_Q = Q_bits[r] >> abs(move)
                    
            
                    if P_bits[nr] & new_Q:
                        overlapped = True
                        break
            
            if not overlapped:
                h = max(N, dr + curr_R) - min(0, dr)
                w = max(M, dc + curr_C) - min(0, dc)
                answer = min(answer, h * w)

print(answer)

'''
4방향

겹치는지 확인은 비트연산으로 최적화
검사 범위 -R+1 ~ N-1, -C+1 ~ M-1
M,C = 5, 3 일때 -2부터 4까지 탐색
-2로 비트이동하려면 왼쪽으로 4칸 보내야함. 4는 오른쪽으로 2칸
이동 거리 : abs((M-C)-dc)

M, C = 3, 5일때 -4부터 2까지 탐색
-4로 비트이동하려면 왼쪽으로 2칸 보내야함 2는 오른쪽으로 4칸
이동거리 : abs((M-C)-dc)
'''