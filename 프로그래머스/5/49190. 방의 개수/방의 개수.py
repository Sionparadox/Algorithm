directions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1, -1], [-1, 0], [-1, 1]]
def solution(arrows):
    answer = 0
    visited_nodes = set()
    visited_lines = set()
    visited_nodes.add((0,0))
    pos = (0,0)
    for arrow in arrows:
        for _ in range(2):
            nx = pos[0] + directions[arrow][0]
            ny = pos[1] + directions[arrow][1]
            next = (nx, ny)
            line = (pos, next) if pos < next else (next, pos)
            if next in visited_nodes and line not in visited_lines:
                answer += 1
            
            visited_nodes.add(next)
            visited_lines.add(line)
            pos = next
        
    return answer


'''
1) 방문체크를 해서 방문했을 때 역추적으로 만들어진 방 체크하기.
    방이 만들어진다 : 한번 방문됐던 점이 재방문됐을 때 발생(이외 경우에서는 방을 만들 수 없음)
대각선으로 찌르면 점이 없는 곳을 꼭지점으로 하는 방이 만들어 질 수 있음 -> 2배처리해서 중간도 점으로 만들어버리기
'''