import sys
input = sys.stdin.readline

class Node:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dir = {
      'A' : None,
      'B' : None,
      'C' : None,
      'D' : None
    }

N, K = map(int, input().split())
moves = input().strip()
plants = [Node(*tuple(map(int, input().split()))) for _ in range(N)]
now = plants[0]

plants.sort(key=lambda p:(p.x-p.y, p.x))
for i in range(1, N) :
    if plants[i-1].x - plants[i-1].y == plants[i].x - plants[i].y :
        plants[i-1].dir['A'] = plants[i]
        plants[i].dir['D'] = plants[i-1]

plants.sort(key=lambda p:(p.x+p.y, p.x))
for i in range(1, N) :
    if plants[i-1].x + plants[i-1].y == plants[i].x + plants[i].y :
        plants[i-1].dir['B'] = plants[i]
        plants[i].dir['C'] = plants[i-1]

def delete(node, d1, d2) :
  if node.dir[d1] and node.dir[d2]:
    node.dir[d1].dir[d2], node.dir[d2].dir[d1] = node.dir[d2], node.dir[d1]
  elif node.dir[d1]:
    node.dir[d1].dir[d2] = None
  elif node.dir[d2]:
    node.dir[d2].dir[d1] = None

for d in moves:
    if now.dir[d]:
        nxt = now.dir[d]
        delete(now, 'A', 'D')
        delete(now, 'B', 'C')
        now = nxt
print(now.x, now.y)   



'''
비숍의 움직임과 같은 방향성을 이용해 x-y, x+y를 키로 하는 딕셔너리를 만들어 정렬
이후 위치에 대해 이분탐색해서 다음 위치를 찾는 방식을 사용했는데 시간초과

이중 연결리스트 사용으로 개선
노드 내에 해당 방향에 대한 다음 노드를 저장.
x-y, x+y로 정렬한 배열을 통해 각각 다음 노드를 변경
삭제 시에는 해당 노드로 연결된 노드들에 대해 이 노드를 건너뛴 다음 노드로 연결시킴
'''