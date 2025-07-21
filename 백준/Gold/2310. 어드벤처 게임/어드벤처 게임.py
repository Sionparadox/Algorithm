import sys
input = sys.stdin.readline

class Room:
    def __init__(self, arr):
        self.content = arr[0]
        self.cost = int(arr[1])
        self.next = [int(x)-1 for x in arr[2:-1]]
    
    def calc(self, n):
        if self.content == 'L':
            n = max(n, self.cost)
        elif self.content == 'T':
            n -= self.cost
        return n

def DFS(idx, money):
    if idx == N-1:
        return True
    
    for nxt in rooms[idx].next:
        if not visited[nxt]:
            new_money = rooms[nxt].calc(money)
            if new_money < 0:
                continue
            visited[nxt] = True
            if DFS(nxt, new_money):
                return True
            visited[nxt] = False
    
    return False 
            
while True:
    N = int(input())
    if N == 0:
        break
    
    rooms = []
    for _ in range(N):
        _input = list(input().strip().split())
        rooms.append(Room(_input))
    
    visited = [False]*N
    flag = DFS(0, 0)
    if flag:
        print("Yes")
    else:
        print("No")