import sys
input = sys.stdin.readline

M = int(input())
K = int(input())

board = [[x-M for x in list(map(int, input().split())) ]for _ in range(8)]

tot = sum(sum(row) for row in board) // 15
R = [0]*8
C = [0]*8

for r in range(8):
    tmp = sum(board[r])
    R[r] = (tmp-tot)//7

for c in range(8):
    tmp = sum(board[r][c] for r in range(8))
    C[c] = (tmp-tot) // 7

for r in range(8):
    ans = []
    for c in range(8):
        k = R[r] + C[c] - board[r][c]
        if k == 1:
            ans.append('+')
        elif k == -1:
            ans.append('-')
        else:
            ans.append('.')
    print(*ans)

'''
분무기 하나 설치할 때마다 총합 +15, -15
tot = 15*('+'수- '-'수)
각 행, 열에 존재하는 분무기의 수
1) tot = 1 (2,1)
3행  : -6
5행  : +15
나머지: +1

행에 없으면 tot와 같음.
행의 변화량은 (행의합 - tot) // 7
열도 동일

행의 변화량 + 열의 변화량 - 자신의 변화량
answer[r][c] = R[r] + C[c] - board[r][c]
'''