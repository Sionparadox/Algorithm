TC = int(input())
for tc in range(1, TC+1):
    D, N = map(int, input().split())
    horse = [tuple(map(int, input().split())) for _ in range(N)]
    time = 0
    if N == 1:
        time = (D-horse[0][0])/horse[0][1]
    else:
        if horse[0][0] > horse[1][0]:
            horse[0], horse[1] = horse[1], horse[0]
        if (D-horse[0][0])/horse[0][1] >= (D-horse[1][0])/horse[1][1]:
            time = (D-horse[0][0])/horse[0][1]
        else:
            time = (D-horse[1][0])/horse[1][1]
    
    print(f'#{tc} {D/time:.7f}')