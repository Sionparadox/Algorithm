import sys
input = sys.stdin.readline

class Dice:
    def __init__(self):
        self.top = 0
        self.side = [0,0,0,0]
        self.bottom = 0
    
    def setBottom(self, n):
        self.bottom = n
    
    def getBottom(self):
        return self.bottom
        
    def printTop(self):
        print(self.top)
    
    def roll(self, d):
        # 0:오른쪽, 1:왼쪽, 2:위, 3: 아래
        temp = self.side[:]
        if d == 0:
            self.side[1], self.side[3] = self.top, self.bottom
            self.top = temp[3]
            self.bottom = temp[1]
        elif d == 1:
            self.side[1], self.side[3] = self.bottom, self.top
            self.top = temp[1]
            self.bottom = temp[3]
        elif d == 2:
            self.side[0], self.side[2] = self.top, self.bottom
            self.top = temp[2]
            self.bottom = temp[0]
        elif d == 3:
            self.side[0], self.side[2] = self.bottom, self.top
            self.top = temp[0]
            self.bottom = temp[2]
          
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
orders = [x-1 for x in list(map(int, input().split()))]

directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

pos = [x, y]
dice = Dice()
for cmd in orders:
    nx, ny = pos[0]+directions[cmd][0], pos[1]+directions[cmd][1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    pos = [nx, ny]
    dice.roll(cmd)
    if board[nx][ny] == 0:
        board[nx][ny] = dice.getBottom()
    else:
        dice.setBottom(board[nx][ny])
        board[nx][ny] = 0
    dice.printTop()
