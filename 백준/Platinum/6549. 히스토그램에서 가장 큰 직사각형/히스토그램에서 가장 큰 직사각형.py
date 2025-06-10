import sys
input = sys.stdin.readline

while True:
    height = list(map(int, input().split()))
    N = height[0]
    if N == 0:
        break
    height = height[1:]+[0]
    
    stack = []
    answer = 0
    for i in range(N+1):
        h = height[i]
        start = i
        while stack and stack[-1][1] > h:
            idx, l = stack.pop()
            answer = max(answer, l*(i-idx))
            start = idx
        stack.append((start, h))
    
    print(answer)

'''
모노토닉 스택 사용

스택에 (인덱스, 높이) 튜플을 저장
스택의 끝이 현재 높이보다 높으면 해당 높이 * 길이로 최댓값 계산
'''