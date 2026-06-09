from collections import defaultdict
TC = int(input())
for _ in range(TC):
    N = int(input())
    x_pos = defaultdict(list)
    y_pos = defaultdict(list)
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    for x, y in arr:
        x_pos[x].append(y)
        y_pos[y].append(x)
        
    answer = 0
    for x, y in arr:
        if len(x_pos[x]) == 1 or len(y_pos[y]) == 1:
            continue
        width = max(abs(x-min(y_pos[y])), abs(x-max(y_pos[y])))
        height = max(abs(y-min(x_pos[x])), abs(y-max(x_pos[x])))
        answer = max(answer, width*height)
    
    print(answer)