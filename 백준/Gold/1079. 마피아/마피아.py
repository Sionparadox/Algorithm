import sys
input = sys.stdin.readline

N = int(input())
guilty = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
player = int(input())

dead = [False]*N

answer = 0
def backTrack(left, k):
    global answer
    
    if dead[player] or left == 1:
        answer = max(answer, k)
        return 

    
    #낮
    if left % 2 == 1:
        max_v = -1
        t = -1
        for i in range(N):
            if dead[i]:
                continue
            if guilty[i] > max_v:
                max_v = guilty[i]
                t = i
            
        dead[t] = True
        backTrack(left-1, k)
        dead[t] = False

    #밤
    else:
        for p in range(N):
            if dead[p] or p == player:
                continue
            
            dead[p] = True
            for i in range(N):
                if not dead[i]:
                    guilty[i] += R[p][i]
            
            backTrack(left-1, k+1)
            
            for i in range(N):
                if not dead[i]:
                    guilty[i] -= R[p][i]
            dead[p] = False
    

backTrack(N, 0)
print(answer)
        

'''
낮, 밤을 나눠서 백트래킹
낮은 분기 없이 선형으로 바로 선택
밤은 죽은사람 빼고 선택, 죽은 사람 guilty = -1
-> 시간초과
dp로 메모이제이션 추가 필요?? -> X 메모리 소비가 너무 큼
어레이 복사를 없애기

'''